#Define a function called shorten_tup that takes a tuple and removes the last item in the tuple


def shorten_tup(tuple1):
    """This function takes a tuple and removes the last item in the tuple"""
    #Tuple -> Tuple
    newTuple = ()
    for value in tuple1:
        if value != tuple1[-1]:
            newTuple += (value,)
    ###You can't reassign a global variables contents inside a function call
    return newTuple



#Functions cannot modify the contents of global variables
#As written these instructions are impossible.
#Tuples and ints floats and strings arwe all inmutable datatypes, which means these values cannot be changed
#You can reassign a variable from one inmutable value to another, but that doesn't work inside a function

#Today we are going to introduce our first mutable data type, the list, which is very similar to the tuple in python
#but it comes with a collection of tools that can modify the type. Also we use square brackets instead of round
#parenthesis

#One of these tools is the del keyword, one of the list methods

def shorten_list(list1):
    """This function takes a list and then shortens it by 1"""
    #List -> None

    del list1[-1]
    return None

####Using the is command to check equality can show whether the variable was defined as another variable, or a
#different thing that holds the same value

#list1 = [1,2,3]
#list2 = list1
#list3 = [1,2,3]

#   list1 == list3     == True
# list1 is list2 == True
# list1 is list3 == false

#append list method

def limited_list(numList, maximum):
    """Returns a copy of numList with all values that are larger than maximum replaced with maximum"""
    # List of nums, maximum -> List of nums
    newList = []
    for val in numList:
        if val > maximum:
            newList.append(maximum)
        else:
            newList.append(val)
    return newList

