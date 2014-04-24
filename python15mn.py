#!/usr/bin/env python
# Written by Cédric Picard, License DWTFYW (2014)

################
# Introduction #
################
# This is an introduction to python3.4 in 10 minutes inspired by the one from
# http://www.stavros.io/tutorials/python/
#
# Python is a mature, widely used language in the opensource world, praised
# for its readability and flexibility. It can be used in any domain and is
# one of the main languages of organisations such as canonical (ubuntu) or
# google (google, youtube). It hass also been used by the MIT to teach
# object-oriented programming for many years and is in constant progression.
# It is installed by default on most linux and unix systems.
#
# Although there are two concurrent versions of python at that time (2.7 and
# 3.4), this tutorial targets the 3.x branch.
#
# Python is a strongly (types are forced), dynamically (a same variable can
# have many  and implicitly (you don't have to declare the type) typed language.
# It is case-sensitive and object-oriented (everything is an object).
# But first of all:

print("Hello World!")
# Hello World!

###############
# Getting help#
###############
# The best place is the online python documentation: https://docs.python.org/3/
#
# Otherwise three functions can help you :
# 'help' returns the documentation of an object
# 'dir'  returns the list of the methodes and attributes of an object
# 'import this' is a reminder to use when in doubt :)

help(5)
# Help on int object:...
dir(5)
# ['__abs__', '__add__', ...]


##########
# Basics #
##########
# Python has no mandatory statement termination characters and blocks are
# specified by indentation. Indent to begin a block, dedent to end one.
# Statement that expects an indentation level end in a colon (:).
# Indentation is usually 4 space wide.
# Values are assigned using '=' and tests are done with '=='. You can
# increment/decrement using += and -=. This works on many datatypes such as
# numbers, strings or lists.

myvar = 3
myvar += 2
print(myvar)
# 5
myvar -= 1
print(myvar)
# 4
myvar = "Hello"
myvar += " world!"
print(myvar)
# Hello World!
myvar2 = 42
myvar, myvar2 = myvar2, myvar
print(myvar)
# 42
print(myvar2)
# Hello World!
myvar = input("Enter a value:\n")
# Enter a value:
# test
print(myvar)
# test

##############
# Data types #
##############
# The main data structures in python are lists, tuples and dictionaries.
# Lists are the most used structure, they are one-dimensional arrays that can
# be composed of any element and have automatic size management.
# Tuples are lists that are immutable (they cannot be changed) and are mostly
# used implicitly, for returning many variables at once or for swapping
# variables values (see previous example).
# Dictionaries are named hash-tables in other languages. They are very easy
# to define in python and thus are heavily used. They can bear any type too.
# Structures that behave as lists (you can iterate on its elements) are
# called iterables.

mylist  = ["item 0", 'one', 2, 3.14, [4.1, 4.9]]
mylist.append(5)
print(len(mylist))
# 5
print(mylist)
# ["item 0", 'one', 2, 3.14, [4.1, 4.9], 5]
print(mylist[3])
# 3.14
print(mylist[-1])# you can count backward with negative numbers
# 5
print(mylist[3:])
# [3.14, [4.1, 4.9], 5]
print(mylist[:3])
# ["item 0", 'one', 2]
print(mylist[:])
# ["item 0", 'one', 2, 3.14, [4.1, 4.9], 5]
print(mylist[::2]) # last parameter is for step
# ["item 0", 2, [4.1, 4.9]]
print(mylist[::-1])
# [5, [4.1, 4.9], 3.14, 2, 'one', "item 0"]
print("Coucou!"[::-1]) # Strings are lists too
# !uocuoC

mytuple = (1, "two", [3])
mytuple2 = 1, "two", [3]
mytuple == mytuple2
# True

mydic = {"key1": 1, 2:["Three"]}
print(mydic["key1"])
# 1
print(mydic[2])
# ["Three"]
mydic[3] = "value3"
print(mydic[3])
# value3


###########
# Strings #
###########
# Strings are lists two. There is no difference between simple and double
# quotes (" and '). Multi-line strings can be defined using triple quotes,
# and strings substitutions can be done using %s.

"""
Hello
"World"    # This takes anything, even quotation marks and this comment !
!
"""

print("I have %s %s." % (1, "apple"))
# I have 1 apple.
print("And me " + str(4) + " durians.")
# And me 4 durians.


################
# Flow control #
################
# Control statements are if, for, while. 'for' works on any iterable, to
# obtain a numerical for, just iterate on a range of numbers given by range()
# 'pass' is a keyword that can be used when there is a need for a statement
# but you want it to do nothing.

# range doesn't exactly return a list but it works exactly the same way.
# That's why we can convert it to a list with 'list' for the sake of printing
print(range(10))
# range(10)
print(list(range(10)))
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

for each in range(5, 10):
    print(each)
# 5
# 6
# 7
# 8
# 9

for letter in "Coucou !":
    print(letter)
# C
# o
# u
# c
# o
# u
#
# !

for numbers in range(10):
    if number in (3, 4, 7, 9) and number > 0 or number <= 2:
        break
    else:
        continue

rangelist = range(10)
if rangelist[1] == 2:
    print("The second item is 2")
elif rangelist[1] == 3:
    print("The second item is 3")
else:
    print("Dunno")

while rangelist[1] == 1:
    pass

#############
# Functions #
#############
# Functions are declared with the def keyword. They can take optionnal
# arguments but cannot be overidden. For named arguments, the name of the
# argument is assigned a value. Functions can return many values by using a
# tuple.
# Lambda functions are anonymous functions that can be useful in a
# functionnal style. Parameters are passed by reference but immutable types
# (tuples, int, strings, etc) *cannot be changed*. This is because only the
# memory location of the item is passed, and binding another object to a
# variable discards the old one, so immutale types are replaced.

def circle(radius):
    return (radius * 3.14 * 2, 3.14 * radius**2)

print(circle(10))
# (62.8, 314)

print(circle)
# < function __main__.circle >

circle = lambda x: x+1
print(circle)
# < function __main__.circle >
print(circle(1))
# 2

def advanced(a_list, an_int=2):
    a_list.append("New item")
    an_int = 4
    return a_list, an_int, a_string

my_list = [3, 4]
my_int = 10
print(advanced(my_list, my_int))
# ([3, 4, "New item"], 4)
print(my_list)
# [3, 4, "New item"]
print(my_int)
# 10

###########
# Classes #
###########
# Python supports a limited form of multiple inheritance in classes. Private
# variables and methodes can be declared, but we mostly rely on conventions
# adding _ or __ before the name to indicate how that it should not be
# modified from the outside.


class MyClass:
    common = 10                     # class attribute

    def __init__(self):             # Constructor self has to be defined
        self.myattribute = 3        # attribute, self has to be defined

    def mymethod(self, arg1):       # method, a reference to the current
        common = arg1               # object is passed in the self argument
        return self.myattribute

    def classmethod(arg1):          # The only difference is how you call it
        common = arg1

class_test = MyClass()              # Instanciation
class_test.myattribute = 5
print(class_test.mymethod(42))
# 5
print(MyClass.common)
# 42
MyClass.classmethod(20)
print(MyClass.common)
# 20

class NewClass(MyClass):            # Inheritance
    def __init__(self, arg1):
        super().__init__()
        common = arg1

##############
# Exceptions #
##############
# Exceptions are try/except/finnaly blocks

try:
    10 / 0       # Raises a ZeroDivisionError
except ZeroDivisionError:
    print("Oops")
else:
    print("What weird mathematics is that ?")
    print("Let's try raising it manually...")
    raise ZeroDivisionError
finally:
    print("We're done")

# Oops
# We're done

#############
# Importing #
#############
# imports are done with the 'import' keyword, if 'from' is used then there is no
# need to specify the namespace.
import random
from time import sleep

sleep(random.randomint(1, 100))

############
# File I/O #
############
# File I/O are very easy in python, but there are two methodes that can be
# used. We'll see the two and prefer the later.

myfile = open(r"./myfile", "w")    # "w" to write, the r"" is the path
myfile.write("coucou\n")
myfile.writelines(["Ahaha\n", "Ohoho\n"])
myfile.close()

myfile = open(r"./myfile")    # default is read, "r" to do it explicitely
print(myfile.readline())
# coucou
print(myfile.readlines())
# Ahaha
# Ohoho
myfile.close()

# or...
myfile = open(r"./myfile")
myfile.read(5)
# couco
myfile.read()
# u\nAhaha\nOhoho\n

# But the best is to use the keyword 'with'
with open(r"./myfile", "a") as f:
    f.write('To append, use "a" instead of "w"')
    f.write("It closes automatically the file")

###################
# Advanced python #
###################
# Do not be afraid ! Python is a powerful language and has many unique
# features. Two of them are heavily used and are part of what we call a
# pythonic style.
#
# The generators are defined using yield instead of return. They are like
# functions but remember where they finished during the last call and start
# from there when called again. They are iterables and are used to spare
# memory, to speed up code and to produce streams of data.

def generator(x):
    yield x-1
    yield x
    yield x+1

    for each in range(5):
        yield each

for number in generator(4):
    print(number)
# 3  # yield x - 1
# 4  # yield x, you can note that it remembered the state of x
# 5  # yield x+1
# 0  # yield each, with each = 0
# 1  # yield each...
# 2
# 3
# 4
# 5

# This will produce the endless stream of all even numbers
def even_numbers():
    i = 0
    while True:
        yield i
        i += 1

for n in even_numbers():
    if n < 10000:            # Well... An infinite loop IS NOT cool.
        print(n)

# Many things are generators in python for performance reason.

# The other important thing to know about are expension lists.
# In math, if asked about every even number in [10,100[, you may write
# something like {10, 12, 14, ... , 98}, but you would rather write the set
# { x | x even, x in [10,100[}.
#
# There is no such thing in C or Java and you have to write a loop... But why
# not using it in python ? This is called a list in intention.

even_list = [ x for x in range(10, 100) if x % 2 == 0 ]
print(even_list)
# [10, 12, 14, ... , 98]

# The condition is facultative
print([x for x in range(5)])

# This is it. There is actually much more to add but most of what you need to
# begin is there.

################
# Unit testing #
################
# To do unit-testing, use the assert statement. The use of a unit-testing
# framework such as pytest or nose is advised.

assert 1==1

##############
# Ressources #
##############
# Here are some ressources about python:
# Books:
#     - Think Python: How to think like a computer scientist (version 3.2)
#
# Websites:
#     - https://docs.python.org/3/                            [en]
#     - http://www.afpy.org/forums/forum_python/forum_general [fr]
#     - http://sametmax.com/                                  [fr]
#     - http://www.blog.pythonlibrary.org/                    [en]
#     - http://www.stavros.io/tutorials/python/               [en]

############
# Skeleton #
############
# Below is a little skeleton to start with
###############################################################################
#!/usr/bin/env python
# This is the best shebang for linux systems.

def main(): # This function is facultative but allows the file to be imported
    pass    # without side-effect, as importation executes the file's content.

if __name__=="__main__": # This structure only launches the main() if the
    main()               # file is explicitely called
