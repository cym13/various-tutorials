========================================
Fusion de nœuds libres en un arbre libre
========================================

Introduction
============

On dispose d'un ensemble de nœuds libres définis par la structure en
pseudo-code suivante :

.. code:: C

    struct Node {
        int      value;         // Valeur
        string   name;          // Nom du nœud
        string   parent;        // Nom du parent
        string[] children;      // Liste de nom des enfants
        Node[]   children_refs; // Liste de références vers les enfants
                                // (employé pour construire l'arbre)
    }

Les nœuds ne sont pas garantis d'avoir des noms différents, il n'est pas
garanti que chaque parent ai un enfant et il n'est pas garanti de n'avoir
qu'une seule racine.

La solution naïve consiste pour chacun des N nœuds à parcourir la liste dans
son intégralité à la recherche de potentiels enfants. Cette recherche est
peu efficace en O(n!) et l'insertion recèle encore des problèmes bien que
d'une complexité moindre.

La principale raison de ce temps est le caractère désordonné des nœuds : nous
allons donc commencer par les trier. Ce tri d'une complexité mineur nous
permettra ensuite une recherche et insertion plus efficace.

.. raw:: pdf

    PageBreak

Tri préliminaire
================

Il y a plusieurs manières de trier les nœuds mais étant donné la nature du
problème nous optons ici pour un dictionnaire. Les complexités relatives aux
différentes opérations avec les dictionnaires python peuvent être trouvées
ici_. Dans le cas moyen une insertion est effectuée en temps constant ce qui
est à notre avantage.

.. _ici: https://wiki.python.org/moin/TimeComplexity#dict

Nous allons trier les nœuds d'après leur parent dans un dictionnaire ayant
pour clés les noms des parents et pour valeur une liste de nœuds ayant un
parent de ce nom. Ces listes seront dénommées "seau".

Afin d'éviter le problème des racines multiples nous aurons une racine
factice nommée "root". Tout nœud sans parent sera affecté à "root".

Il n'est pas possible de corriger le problème des nœuds de même nom et de
parent de même nom. En effet affecter un nouveau nom empêche le parent de
retrouver son enfant dans le futur. Le mieux est de signaler le problème.

L'opération en est grossièrement la suivante :

.. code:: python

    def prepare(unsorted_nodes):
        sorted_nodes = { "root" : [] }
        for node in unsorted_nodes:
            parent = node["parent"]
            if parent == "":
                parent  = "root"

            if parent not in sorted_nodes:
                sorted_nodes[parent] = []

            for children in sorted_nodes.get(parent, []):
                if node["name"] == children["name"]
                    print("Conflict:", node["name"], node["parent"])

            sorted_nodes[parent].append(node)

On effectue l'opération d'insertion une fois pour chaque nœud, aux
opérations secondaires près ce tri est donc en O(n) dans le cas moyen.

Notons qu'à cette étape la seule certitude est que les nœuds d'un même seau
ont un parent de même nom, pas qu'ils partagent le même nœud parent.

.. raw:: pdf

    PageBreak

Construction de l'arbre
=======================

La construction de l'arbre proposée ici se fera par étage. S'il n'est pas
certain que ce soit la méthode optimale ce n'est pas non plus une mauvaise
méthode.

Nous allons nous baser sur 2 structures de données complémentaires.

Un arbre libre
--------------

Ceci est l'arbre dans lequel nous allons insérer les nœuds. À l'origine il
sera composé uniquement du nœud "root". Il contiendra le résultat final après
fusion.

Une file d'insertion
--------------------

Afin de tenir compte de quel nœud a quel parent nous allons les enfiler au
fur et à mesure. La stratégie est d'enfiler chaque groupe d'enfant après
leur parent pour construire l'arbre étage par étage en assurant que tout les
enfants ayant un parent sont traités et que leurs parents sont déjà dans
l'arbre en attente de l'insertion. Les enfants sont enlevés des seaux pendant
leur enfilage.

.. image:: https://c1.staticflickr.com/1/170/456474931_0356ba4a8d.jpg
    :width: 20%

Une garantie intéressante donnée par cette méthode est que si à la fin de la
fusion il reste des nœuds non placés dans l'arbre ces nœuds sont assurés
d'avoir un parent absent de l'arbre. En effet dans le cas contraire ils
auraient soit été des racines et donc affectés à "root", soit insérés dans
l'arbre pendant le traitement de leur parent.

L'insertion en elle-même présente une légère subtilité qui est que l'on ne
souhaite pas re-parcourir tout l'arbre à chaque fois. Pour cela une solution
est de garder une référence vers le parent au moment où l'on trouve son
enfant puis d'enlever celle-ci à l'insertion.

.. raw:: pdf

    PageBreak

.. code:: python

    def build(sorted_nodes):
        # Initialize the root node
        root = Node("root")
        root["children"] = sorted_nodes["root"]
        queue = [root]

        while queue:
            parent = queue.pop(0)

            # We need to copy the list not to iterate on something we change
            for child in sorted_nodes[parent["name"]].copy():
                if child["name"] not in parent["children"]:
                    continue

                sorted_nodes[parent["name"]].remove(child)

                child["_parent_ref"] = parent

                queue.append(child)

            # Insert parent through the saved reference
            parent["_parent_ref"]["children_ref"].append(parent)

            # Remove reference to parent
            parent.pop("_parent_ref")

On lit chaque nœud exactement une fois (linéaire) puis on l'insère via une
référence directe sans parcourir l'arbre ne serait-ce qu'un peu (constant).
L'insertion se fait donc en O(n) dans tout les cas.

Conclusion
==========

Le tri préliminaire était en O(n), l'insertion en O(n) dans le cas moyen.
Cette technique de fusion est donc en temps linéaire dans le cas moyen.

Le pire cas pour les dictionnaires est difficile à atteindre car il nécessite
des collisions de hash à répétition mais s'il est atteint alors toute
insertion dans le dictionnaire est en O(n) et plus O(1) de sortes que le tri
initial est effectué en 0(n!) ce qui amène une complexité totale de O(n!).
