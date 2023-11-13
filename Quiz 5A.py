#Jonathan Wells and Predescu Alimin
#Quiz 5A

#Define a function called shorten_tup that takes a tuple and removes the last item in the tuple


##def shorten_tup(tuple1):
##    """This function takes a tuple and removes the last item in the tuple"""
##    #Tuple -> Tuple
##    newTuple = ()
##    for value in tuple1:
##        if value != tuple1[-1]:
##            newTuple += (value,)
##    ###You can't reassign a global variables contents inside a function call
##    return newTuple
##

#This does not work, becuase the variable does not actually get changed^^^



#Quiz5A
def limit_list(numList, maximum):
    """Replaces all values in numList that are larger than maximum with maximum"""
    #list of numbers, maximum -> None
    counter = 0
    for val in numList:
        if val>maximum:
            numList[counter] = maximum
        counter += 1
    return None
    


def remove_neg(numList):
    """This function removes all negative numbers from numList"""
    #List of numbers -> None
##    i = 0
##    while i in len(numList):
##        if numList[i] < 0:
##            del numList[i]
##        i += 1
    #this fails because everytime we remove an item from this list the index goes up by one, but the indexes of
    #the list were moved left
    #Solution 1
    i = 0
    while i<len(numList):
        if numList[i] < 0:
            del numlist[i]
        else:
            i += 1
    #solution 2, loop through the list starting at the end(-1)
    #Solution 3, make a copy of the list and use the copy for the values and look up their current index
    
