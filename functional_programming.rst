===================================================
A Reasonable Introduction to Functional Programming
===================================================

Introduction
============

I have a friend that is great at programming. I have always liked talking with
him about programming, design and paradigms because he has quite an insight
on these topics and an interesting experience of C, C++ and python among
other languages. But he never used any functional language, and I kept teasing
him on that point, so when he told me that he was actually considering
learning a bit about functional programming I decided to find the perfect
tutorial.

Guess what? I found nothing.

Oh, well, I did find things but it was always doing things in reverse: "Here
is how to do recursion and here is a map and a filter, now go programming son!"

Functions and constructs usualy shown is tutorials are **consequences** and
should not be presented as the essence of functional programming. Would you
teach a newcommer about Object Oriented programming by showing him the
Commander Design Pattern and how to write Getters and Setters? Or would you
start by explaining what problem we are trying to solve with this tools?

So here it is. This is what I consider a good introduction to Functional
Programming. Haters gonna hate. The point is that functional programming
isn't even that well defined so we won't reach a universal consensus either
way (and that's why I won't try by any means to reach such consensus).

The first step is to choose a programming language. I hesitated between
Haskell (the heir of functional programming), Scheme/Lisp (because I love it
and it renders very well the troubled relation that we have with functions),
D (because it's a good language that has many possibilities such as
restricting yourself to using pure functions and immutable data).

As always when I hesitate, I'll go with Python3. "Oh man, python is not
explicitely typed, is as mutable as one can be, lacks most common
functional functions and Guido doesn't like functional programming at all!"

One of the key points that I will be trying to make is that **functional
programming is a style** that can be used in any language.

So let's start!

Why should one care?
====================

This is the most important question. Why should you bother reading all that
stuff anyway? Scott Wlaschin wrote a very interesting article about that
titled `Is your programming language unreasonable?
<http://fsharpforfunandprofit.com/posts/is-your-language-unreasonable/>`_
that I really encourage you to read. I hope he won't mind if I take some of
his examples here.

.. code:: python

    x = 2
    do_something(x)
    y = x-1

So tell me, what is the value of y? 1?

What if I show you the whole code?

.. code:: python

    def do_something(x):
        if x < 32:
            x = False
        else:
            x = True

    x = 2
    do_something(x)
    y = x-1

So here, not only did we change the value of x, we also changed it's type and
then we are using this type as an integer (False is equal to 0) so y finally
equals -1.

Ok, let's do another one:

.. code:: python

    cust_1 = Customer(99, "J.Smith")
    cust_2 = Customer(99, "J.Smith")

    cust_1 == cust_2

What do you say? Are they equal?

Actually, we have no way to tell. We don't even know if the code is valid. Is
the __equal__ method defined for the class Customer? Or the __cmp__ method?
Which will be called if one was removed? What do they do exactly?

I won't go any further, Scott Wlaschin does it better than me. I think that
these examples are enough to show that there is a difficulty here. I'm not
saying that the whole design of python as a dynamic object-oriented language
is nothing but shit because I like python and I know that this design is
being supported by many good arguments.

However, we should never forget that we are not here to write classes (don't
be java), we are here to manipulate data (this is what programming is for)
and designs are here only to help us reduce the complexity inherent to these
manipulations. By reducing the complexity, we reduce the possibility of
mistakes at its source.

At the beginning of programming, the lack of mechanisms for abstraction as well
as the lack of performance to support these abstractions lead us to a way of
thinking about programs that was very close to the machine, fiddling with
assembly and cheap optimisations. This is what gave C, C++, java and many of
the cool guys of today.

Languages that took another approach and favoured expressiveness over machine
code like Lisp or Smalltalk were tagged "to slow to be useful" and mostly
forgotten.

Imperative programming made it's time, but the lack of good scoping tools
made it difficult to reason about how data was processed: there were too many
moving parts.

Object-Oriented Programming offered a way to handle this problem by
encapsulating the moving parts into objects. That way, it was still moving
like hell but we could manipulate the moving parts as a whole.

That worked quite well compared to imperative programming, but as the
examples above show very well, hiding complexity is not reducing it.

Functional programming is another possible solution that tries to handle
complexity by reducing the number of moving parts.

**Functional programming is all about immutability.**

The beginning of an answer
==========================

We will start our journey by stating some simple, fundamental style rules.

Immutability
------------

As we said before, the ability to change the value of something after it's
been declared is a moving part that introduces complexity. It may seem mad,
but let's decide that we won't ever change the value of a variable.

Immutability can't be enforced in python so we will do it by convention.

So, can we still do things that way? This is actually very similar to what is
done in mathematics: once you declared that a=5 you don't go changing its
value, you combine it to get other values. So now we need a way to combine
things.

Pure functions
--------------

"Function" is generaly badly defined. What we call "function" in most
languages actually are procedures: portions of code that can take arguments,
operate arbitrary instructions on these arguments in and out the scope of the
portion of code and return a value or not.

What we call "pure function" (which will be only "function" for the rest of this
article) is the same thing as a function in mathematics: it always returns a
value, it does nothing outside its scope and for a given argument is will
always return the same value. Also a pure function can only call pure functions.

Actually, most of those properties are consequences of our choice of
immutability: what would a function that does not return a value do if it
can't change the state of its arguments? Why would a function that cannot
change the state of anything need to act outside its scope? And for a
function not to always return the same value for the same arguments it would
need some notion of an internal state that would be changed between calls.

So with our hypothesis of immutability we can see that pure functions are
logical consequences.

One should note that another consequence is that any function that doesn't
take any argument is constant (it always return one only value, such as
lambda x: 1). One could also note that accessing a global *constant* from
the inside of a function does not break it's purity.

Pure functions are cool. They have one very neat property which is that they
don't have any side effect, no matter in what condition a function is called
it will not be affected by this condition and it will not change it in any
way. Therefore, they have a replacement property: one can always replace the
call to a function by it's result and that in any condition.

.. code:: python

    mul(sub(34, 15), add(12, 8)) <=> mul(19, 20) <=> 380

We will talk more about their properties later, but let's notice that it is
really difficult to use nothing but pure functions. 'print()' and 'input()' for
example are not pure functions, they return values that are not garanted to
be always the same and they modify things out of their scope.

We will have to compose with such difficulties but the key point is here to
limit as much as possible their impact.

Recursion
---------

One of the first thing that comes to mind when discovering computations with
immutability is the problem of loops. How do one loop over a variable when
one can't change the value of this variable?

The answer is simple: he doesn't. Instead of describing how to change data,
let's *describe* into what it is transformed.

The main way to do this is through recursion.

Now I won't offense you by presenting an example of recursion, instead I'll
let you write one.

Here, write one.

The first that comes to your mind.

Really, I mean it.

I'm done talking until you have written an example.

...

...

...

Are you done?

Ok, so let me say this straight:

**Your example is pure shit.**

I'm quite sure you coded a factorial or a Fibonacci function. Something like:

.. code:: python

    def factorial(n):
        if n == 0:
            return 1
        return n * factorial(n-1)

It is pure shit.

It is recursion, okay. And it is pure, that's cool. But it has a *huge*
space (memory) complexity in O(n) compared to its time complexity (also
almost O(n)).

It's okay, your prefer loops after all and you were always told to avoid
recursion because of this problem of space complexity. It is a problem
inherent to recursion, you couldn't do better, that's why functional
programming is so useless.

Well, I'd like to prove to you that all of this is false with a little
example.

Let's say that we don't have any way to add two numbers. We want to create a
function add(n, m) that takes two numbers and returns the sum of the two.
The only primitive we have is a function inc(n) that takes a number n and
returns n+1.

.. code:: python

    def inc(n):
        return n+1

How would you design the add function ?

There are two main ways to do it. Here is the first.

.. code:: python

    def add(n, m):
        if m == 0:
            return n
        return inc(add(n, m-1))

As we said, with pure functions we can replace everything by its value, let's
work it out for add(8, 5):

.. code:: python

    add(8, 5)
    inc(add(8, 4))
    inc(inc(add(8, 3)))
    inc(inc(inc(add(8, 2))))
    inc(inc(inc(inc(add(8, 1)))))
    inc(inc(inc(inc(inc(add(8, 0))))))
    inc(inc(inc(inc(inc(8))))))
    inc(inc(inc(inc(9))))
    inc(inc(inc(10)))
    inc(inc(11))
    inc(12)
    13

The number of lines shows the time complexity, the length of lines shows the
space complexity. Each grow in O(n).  This is similar to what you first did
with your factorial-like example. As the function cannot have any state it
manages complexity by stacking values.

Here is another way to do it:

.. code:: python

    def add(n, m):
        if m == 0:
            return n
        return add(inc(n), m-1)

We didn't change much, let's unwind add(8, 5):

.. code:: python

    add(8, 5)
    add(inc(8), 4)
    add(9, 4)
    add(inc(9), 3)
    add(10, 3)
    add(inc(10), 2)
    add(11, 2)
    add(inc(11), 1)
    add(12, 1)
    add(inc(12), 0)
    add(13, 0)
    13

As we can see, the time complexity of this function is exactly the same as
before, meaning that we won't gain any time by using it instead of the first
one. However, we can see that space complexity never actually change, it is
constant, in O(1).

This recursion is designed so that it never actually stacks data. It is
called **tail recursion** and it was theoretically shown that it is always
possible to write such a recursion.

(As a side note, it was also shown that any loop can be transformed into a
recursion and inversely.)

Let's see how to do it for the factorial example:

.. code:: python

    def factorial(n, accumulator=1):
        if n == 0:
            return 1
        return factorial(n-1, accumulator*n)

See? Not that hard isn't it?

It should be noted that in many languages that are functional
programming-oriented recursions are automatically optimised into tail
recursions at compile time. This is not the case in python.

Functions as data
-----------------

As you can now imagine, we make a heavy use of functions in functional
programming. This functions are treated in a different way than data in many
languages, by what I mean that you can assign a number as value to a variable
but you usually can't assign a function as value to a variable.

Languages that doesn't treat functions differently from other data are said
to have **Higher-order functions**. This is an important property that will
allow us to pass functions as arguments, to build functions on the fly etc...

Lambda functions are anonymous functions ; functions that are created as data
without being assigned a name. In python, the two following syntax are alwost
equivalent (their differences doesn't have any impact at our level):

.. code:: python

    def double(n):
        return n*2

    double = lambda n: n*2

We will make a heavy use of those from now on.

Note that lambdas are somehow linked to another property of the language: the
ability to declare functions inside other functions:

.. code:: python

    def mult_by(n):
        def mult(x):
            return n*x
        return mult

    double = mult_by(2)

    double(5) == 10

This will prove very useful later when discussing closures.

Side effects of Functional Programming
======================================

Functional programming do not have side effects on the runtime environment,
but is has *huge* side effects on the way one programs and on the properties
of such programs!

Easier composition!
-------------------

First of all, composing stuff is easier.

Let's start by writing a helper function that is not standard in python (but
really should) named 'chain' based on the 'reduce' function that we will
discuss later:

.. code:: python

    from functools import reduce

    def chain(*functions):
        return reduce(lambda f,g: (lambda *x: g(f(*x))), functions)

It is ok not to understand it yet, you can always come back at the end. The
point of this particular function is to illustrate a concept that is not
dependant of its implementation.

While not perfect, this function acts like the pipe "|" of Unix shells, it
chains function and returns a function that combines the others:

.. code:: python

    inc    = lambda x: x+1
    double = lambda x: x*2
    triple = lambda x: x*3

    my_fun = chain(double, inc, triple)

    my_fun(5) == 33

The parallel with Unix shells was not accidental, everything that is good in
the Unix philosophy ("Build little programs that do only one thing but do it
well and combine easily with others") is true here. Piping data from one
program to another has proved to be a very good way to handle complexity,
that's why command-line utilities are still used today.

Furthermore, remark that we are being lazy here. If we want to describe some
transformation on an object, we do not build any temporary state, we only
compute the new data when we need it.

Building functions instead of building states increases performance,
expressivity (we will talk about it later), it also fits well with itself.
What I mean by that is that we are composing functions with functions... so
the resulting functions can also be composed to get more functions! And this
costs nothing.

It is often useful to prepare part of the arguments of a function. One way to
do it is:

.. code:: python

    # Preparing arguments in map
    double_all = lambda lst: map(double, lst)

    double_all([2, 3, 4])  ->  [4, 6, 8]

This may work for little examples, but you may prefer using a partial:

.. code:: python

    from functools import partial

    double_all = partial(map, double)

    double_all([2, 3, 4])  ->  [4, 6, 8]

Another way to compose things is by wrapping them together:

.. code:: python

    def sandwich(food):
        return lambda : list("bread", *food(), "bread")

    def cheese(food):
        return lambda : list("cheese", *food(), "cheese")

    # Let's wrap things together
    def ham():
        _ham = lambda : ["ham"]
        return sandwich(cheese(_ham()))

    # The same wrapping using python's decorator syntax
    @sandwich
    @cheese
    def ham():
        return ["ham"]

    ham() == ["bread", "cheese", "ham", "cheese", "bread"]

Easier parallelisation!
-----------------------

There are thee generic functions that are interesting enough to be considered
a key point of functional programming: map, filter, reduce.

Map is the functional compositor by excellence, it takes a function and a
list of elements and returns the list of the evaluations of the function on
this elements.

Long story short:

.. code:: python

    map(double, [1, 2, 3, 4, 5]) == [2, 4, 6, 8, 10]

This seems pretty simple, why would it be a key point? Well map is a perfect
example of how things are handled in functional programming. It is a pure
function that takes a pure function and abstract an implementation to focus
only on the transformation of data. You don't know how map is implemented,
and you most surely wouldn't care less, but it expresses a solution more
beautiful than a for loop.

.. code:: python

    tmp_lst = []
    for each in [1, 2, 3, 4, 5]:
        tmp_lst.append(double(each))
    return tmp_lst

That way of writing things hides the real meaning of the action: applying
double to an array.

**Any time you need to transform a list into another list,
map is there for you**

Another function with the same properties of map is filter. Filter does what
it says it does, it takes a function and a list and filters the list
returning only the elements that corresponds to a positive return value of the
function passed as argument.

.. code:: python

    def even(n):
        return True if n % 2 == 0 else False

    filter(even, [1, 2, 3, 4, 5]) == [2, 4]

**Any time you need to select only some elements from a list,
filter is there for you**

The last one is reduce that we already used once. Reduce takes a function and
a list of arguments and combines the arguments two by two with the function to
produce a single value as result. It operates from right to left.

.. code:: python

    from functools imports reduce

    reduce(sum, [1, 2, 3, 4, 5]) == reduce(sum, [3, 3, 4, 5])
                                 == reduce(sum, [6, 4, 5])
                                 == reduce(sum, [10, 5])
                                 == reduce(sum, [15])
                                 == 15

Other programming languages have different names for these functions, reduce
is often called foldl or fold-left in what case it comes with its counterpart
foldr or fold-right. This is the same as reduce but it operates from left to
right.

**Any time you need to transform a list into a single object
reduce is there for you**

Together these functions describe a very common design pattern to manipulate
data: filter-map-reduce

We have a bunch of data. First let's get only the one that we find
interesting, then format these one to get new data and reduce it to a single
value (by averaging or anything).

A shell example of filter-map-reduce could be:

.. code:: shell

    grep filter file | tr '"' '\n' | grep -c reduce

While interesting and expressive by themselves, this functions takes all the
more importance when dealing with parallelisation.

Remember that we are only using functions that have no state whatsoever, so
running them concurrently is the easiest thing of the world! For example, in
the programming language Erlang, each function runs concurrently by default
so any function can be replaced at runtime without any second-thought.

Furthermore map and filter propose transformations that are very easy to run
in parallel over the whole array, that's why filter-map-reduce became a
standard paradigm of big data, it could be run massively in parallel even on
different computers and still be reduced to a single result at the end.

To do that in python you want to see the map method of multiprocessing.Pool
and its variants which implements a concurrent map.

This popular construct is present in python natively through list
comprehensions:

.. code:: python

    inc  = lambda n:   n+1
    even = lambda n:   True if n%2==0 else False
    add  = lambda a,b: a+b

    transform = chain(partial(filter, even),
                      partial(map,    inc),
                      partial(reduce, add))

    transform(range(5)) == 8

    sum(inc(n) for n in range(5) if even(n)) == 8

Easier laziness and streams!
----------------------------

Another cool thing about pure functions is that each call is independant.
Take the map example for example, the order in which the elements are
computed isn't important as one value never depends on another one.

Therefore it is easy to be lazy as we know that we can compute that value at
any time.

Also, as the output of a pure function is always the same for a given input
one can cache results instead of recomputing it each time. This is called
memoization and is completely impossible to do safely with non-pure functions.

In python, this is done with the functools.lru_cache decorator:

.. code:: python

    from functools import lru_cache

    @lru_cache()
    def fib(n):
        if n<2:
            return n
        return fib(n-1) + fib(n-2)

This is a great way to increase performance.

However, there is one that seems impossible with our pure function: dealing
with an infinite list of numbers.

The stream paradigm is well represented in python through generators:

.. code:: python

    def numbers():
        i = -1
        while True:
            i += 1
            yield i

    for n in numbers():
        print(2*n)

    # Prints the list of all even numbers without stopping

This can't be achieved without introducing mutability. However one way to
control its complexity is to use a closure to restrict the scope of the
mutable section:

.. code:: python

    def gen_numbers():
        i = -1
        def numbers():    # This is a closure, even if i was defined outside
            i += 1        # the scope of 'numbers' it is still bound to its
            return i      # instance and no other.
        return numbers

    print_even = chain(gen_number(),
                       double,
                       print)

    def print_even_numbers():
        print_even()
        return print_even_numbers()

Ok, there is no reason in python not to use classic generators, but I think
that this was a neat example to demonstrate closures. The way such things are
treated in programming languages with no side effect like haskell is through
monads which are a really cool thing but are too wide a subject to fit in
such an introduction. Just remember that they are used to rescrict unpure
things within known scope without allowing them to mix with pure stuff.

Easier unit testing!
--------------------

Unit testing is great. It forbids regressions and allows many programmers to
define interfaces and then work separately while keeping the whole code
coherent. But is not something that is as wildely used as one could think.
And if your project is using unit testing, answer honestly this question: is
there not a single function that you decided not to write tests for?
Why is that? Sure, programmers are lazy animals and don't like writting
dead code but they also are rational so why aren't they doing more unit
testing?

My opinion is that most of the time is is just too hard to do. Unit testing
object oriented methods and stateful objects is only possible by mocking the
anticipated environment in which the object will be called. Moreover theses
programming styles encourage long and complex functions which result in many
corner cases.

By encouraging short, independant functions, functional programming is well
adapted to unit testing which pushes code safety even further.

By using pure functions a whole class of errors just disappear. It's not that
their complexity is hidden behind the curtains, it was effectively reduced.

Readibility for the win!
------------------------

We slightly shifted on this subject before but let's say it straight:
functional programming is by essence a paradigm that encourages readability
(and that should talk to any python developper).

By focusing more on the goal than on the way to achieve it it often become
declarative and very expressive.

Take the Fibonacci example:

.. code:: python

    # Imperative style
    def fibonacci(n):
        tmp_1  = 0
        tmp_2  = 1

        if n == 0:
            return 0
        if n == 1:
            return 1

        for _ in range(n):
            result = buf_1 + buf_2
            buf_2  = buf_1
            buf_1  = result

        return result


    # Without tail recursion
    def fibonacci(n):
        if n == 0:
            return 0
        if n == 1
            return 1
        return fibonacci(n-1) + fibonacci(n-2)


    # With tail recursion
    def fibonacci(n, curr=0, next=1):
        if n == 0:
            return curr
        return fibonacci(n-1, next, curr+next)

Not only is the code more concise in functional style, it is also blazzingly
similar to the mathematic definition of the Fibonacci sequence. We're not
dealing with the problem of temporary values at all, we just declare what we
want it's value to be in each case.

**Stop thinking in steps, start thinking in transformations**

Allow me to take an example from the excellent post `Why Every Language Needs
Its Underscore
<http://hackflow.com/blog/2014/06/22/why-every-language-needs-its-underscore/>`_
from Alexander Schepanovski:

.. code:: python

    # Checks if a sequence is ascending

    prev = None
    for x in seq:
        if prev is not None and x <= prev:
            is_ascending = False
            break
        prev = x
    else:
        is_ascending = True

    # Becomes

    is_ascending = all(l < r for l,r in pairwise(seq))

    # With

    def pairwise(lst):
        for i in range(len(lst)-1):
            yield lst[i], lst[i+1]

Here all returns True if all elements of an iterable respect a given
condition and pairwise is used to get a sliding window of two elements.

More theoretical bases
----------------------

When first defining the bricks of functional programming we made a lot of
comparisons with mathematics. This was no coincidence. Forcing our tools to
behave according to mathematical principles allows as to reason mathematically
about them.

This doesn't only mean that one can reason about programs without having an
actual running computer to try things out, that also means that we can have
mathematical certitudes about the transformations that occur.

Having your process formally proved isn't just an assurance of quality, it is
also a guarantee that your program won't ever have a bug (in the scope of the
study of course).

Monoids, monads, type and category theories are cool things, and very deep
too. Of course you can go and use functional programming without actively
dealing with those but if you want it to be as profitable as possible then
you will have to confront it someday.

The counterparts of Functional Programming
==========================================

Let's conclude on the counterparts. The first one is performance. Of course
as we seen many arguments against performance in functional programming don't
stand, but truth is that at some point your beautiful abstraction will have
to get converted into machine code and fiddling with bytes is hard.

Also, it is a totally different way of thinking. This can be a problem when
programming whith other people that may not share your point of view on
program designs. This can also be an issue when programming with a language
that is not at all thought functionally (lack of lambdas, closures, type
checking, functional constructs).

But in the end I think that knowing functional programming is worth the time
spent learning it. At the very least it should let you see problems under
other angles.

Some links to conclude
======================

To the links that I already spread into the article I would add:


`Abstracting control flow
<http://hackflow.com/blog/2013/10/08/abstracting-control-flow/>`_

`The curse of the excluded middle 
<http://queue.acm.org/detail.cfm?ref=rss&id=2611829>`_ which is also a great
introduction to monads.
