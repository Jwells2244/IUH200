#A function has a name, which is really just a variable that stores a function object
# You turn a function into a command to use that function by calling that function
# which just means putting it before a pair of parenthesis, and if there are arguments
# that need to be passed, that is included inside the parenthesis

# The data that is passed to a function are called arguments, and we say that in
# a function call, the arguments are passed to a function

# Most functions have some kind of output/return data that is returned by the function call
# so that returned value can be used in other commands or stored to a variable, or just ignored

# Creating a function

def square (num):
    #this function calculates the square of num
    return num**2


#The comment "This function calculates the square of num." is called a purpose statement
# which is just a description of what the function does. In addition to a purpose statement,
# it's often useful to include a comment describing what types of the input arguments are meant to be
# and what type is meant to be returned by the function, and we often format this kind of type
# information using a *signature*. So we could represent the intended signatures for our square function
# int -> int
#float -> float
# complex -> complex
# OR we could shorten all this and cover a number of other different possibilities by using a shorthand
# for the category of all types that you can arithmetic with:
# Number -> number

# In this class, you must always include a signature in your comments for defining your function.
#Terminology:
#The first line of a function definition is called the header of the definition, and the rest of the definition
# is called the body. In python, the body must be indented

###########

#Detour: line breaks in strings
#If you wanted to display this on a screen as a part of a script

# Line 1
# Line 2
# Line 3


#Another method
# Use """triple quotes""" or '''triple quotes'''

#To split python statements between line, you can use a backslash to be able to make things multiple lines

#Back to function definitions

# If you want to include some documentation that can show up in tooltips, or when using the help function
# we should format our comments as a *docstring*
#When the first line of a function definition body is just a string by itself, when that happens, Python will
# automatically treat that string as the *docstring*

##def square(num):
##    "This function calculates the square of num"
##    #Number -> number
##    return num**2

#In this class you will be expected to include a docstring with a purpose statement and a signature for ebery
# function you define

# Quiz Work:
# Define a function that calculates the volume of a box that calculates based on its length width and height

def volumeOfBox(length, width, height):
    """This function calculates the volume of a box using it's length, width and height
    Number, Number, Number -> Number
    All Arguments should have the same units, and the output is in that unit cubed"""
    return(length*width*height)

    

