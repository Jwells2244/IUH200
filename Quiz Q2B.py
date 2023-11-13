# Jonathan Wells and Jack Tyndall

#Quiz Q2B
#Take the function that you defined last time to calculate the volume of a box
# and use that to create a script that asks the user to enter in 4 things, a density
# a width, length, and height and then calculate the mass of a block of that size with that density

def volumeOfBox(l, w, h):
    """This function calculates the volume of a box using it's length, width and height
    Number, Number, Number -> Number
    All Arguments should have the same units, and the output is in that unit cubed"""
    return(l*w*h)

lengt = float(input("What is the length of the block(cm): "))
width = float(input("What is the width of the block(cm): "))
height = float(input("What is the height of the block(cm): "))
density = float(input("what is the density of the material (in g/cm^3): "))

print("The block weighs " + str((float(volumeOfBox(lengt, width, height)) * density)) + "g")

#Pure functions are functions that take arguments and return a value, but don't
# take any actions (like printing on the screen or getting user input). This includes
# functions like volume(), bin(), and the basic constructors int(), str(), etc.

# Functions that have side effects are not pure functions. Side effects are
# additional actions (other than returning a value) like: user output: displying
# things on the screen, writing to disk, using a physical printer, playing sounds, opening a window
# sending info over a network,
# Or changing what's stored in memory

# For the first few weeks, we'll only be defining pure functions, so you should not be using
# print() or input() in any of your function definitions.

def f(x):
    """this doesn't do anything interesting; it's just to demostrate something"""
    squared = x * 2
    return squared
# The variables x and squared are defined while the function is running, but after
#the function finished and returns its value, they are returned to the state of not being
# defined. So you can't reference those variables after the function finishes running

#x and squared are *local* variables meaning that their scope is just the body of the function definition
# they are defined in

# A global variable is one that has a scope that is the entire script

# This is a global variable

global_y = 100

print("global_y is currently: " + str(global_y))

def g(x):
    """This functions returns the value of the global y variable, plus this functions input: x"""
    print("The function g was just called and now global_y is: " + str(global_y))
    return global_y+x

print("calling g(10)")
print("g(10) = " + str(g(10)))
print("global_y is currently: " + str(global_y))

#In this version of Python, if you ever try to redefine a global variable inside of a function definition
# then Python treats that variable as a local variable for all of that function definition, ignoring the global
# value. But when the function finishes running, the global variable goes back to it's original value


#########

# Tuples
# n -- tuple
# Tuples are inmutable
# Tuples are sequence types, like strings
# and we create tuples using parenthesis
# Tuples indexes start at 0

# We can access the values in a tuple or characters in a str using indexes: t1[1] or letter[4]

# Tuples and strings are also containers, which includes all sequences as well as some other collection
# types that don't have orders to them, like dictionaries and sets. You can use the len() function to obtain
# the number of items in any container.



