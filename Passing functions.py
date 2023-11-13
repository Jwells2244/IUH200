

#Remember you can assign functions to variables with the class of 'function'
def square(n):
    return n*n

#Max function will returns what biggest in a list of numbers, and with a list of strings, it will find the last letter of
#the alphabet
#Can use an optional argument key, can do key=len to determine the max length of the string list instead

##def apply_to_all(list1, f1):
##    """This function takes a list of numbers and it's going to take a function(f1)
##    and apply it to every item in list1, and return a list of the results"""
##    #List of nums, function -> List of nums
##    newList = []
##    for num in list1:
##        newList.append(f1(num))
##    return newList


#Really, this list isn't about numbers. We can be more versatile in purpose statement and signature,
#but we do have to be careful. The above function claims to work on any list of numbers and any function,
#but it doesn't work with all functions. So how do we say what kind of function it works with?

##def apply_to_all(list1, f1):
##    """This function takes a list of numbers and it's going to take a function(f1)
##    and apply it to every item in list1, and return a list of the results"""
##    #List of nums, (number -> number) -> List of nums
##    newList = []
##    for num in list1:
##        newList.append(f1(num))
##    return newList

#If we want to communicate that this works with things other than numbers, we can do this in our signature
#using a parametrized signature
#We can do this in our signature using a 'parametrized signature' like this ???
#When one of the arguments in our function is itself a function, instead of just writing function in the signature


def apply_to_all(list1, f1):
    """This function takes a list of numbers and it's going to take a function(f1)
    and apply it to every item in list1, and return a list of the results"""
    #List of ???, (??? -> ???) -> List of ???
    newList = []
    for item in list1:
        newList.append(f1(item))
    return newList


#Quiz 8A

def apply_twice(x, func):
    """This function returns what happens when you run x through func, and then running that result through func
    again"""
    # value, (value -> value) -> value
    
    return func(func(x))

#The map function returns a special itereable object (of type map) that, when you loop through it,
# runs each of the values in the given iterable through the given functions and uses that resulting value

#The lambda keyword creates a function with a singlem command, without giving a name to that function

#What does the signature of the map function look like?
# (X -> Y), iterable-of-X  -> map-of-Y


