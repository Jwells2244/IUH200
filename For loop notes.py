#Jonathan Wells and George


#container types: str, tuple, list, set (an object that has other objects in it
# sequence types: str, tuple, list (the objects come in a particular order
#iterable types: str, tuple, list, set, dict ... (object that can be "iterated" over using a for loop, has a way to pick
#the next object and know when it's done

def transformedCharacter(char):
    """this function takes a char and returns a version of char that might be turned into a digit from a letter"""
    # Str -> Str
    if char == "o" or char == "O":
        return "0"
    elif char == "i" or char =="I":
        return "1"
    elif char == "e" or char == "E":
        return "3"
    else:
        return char

#You cannot use or without another full statement, ex NOT char == "e" or "E", instead char == "e" or char == "E"
#This script asks the user for a string, transforms each character via transformed_char and prints the results

##userString = input("Please input a string: ")
##for cha in userString:
##    print(transformedCharacter(cha))

def transformed(s):
    """Returns a transformed verison of the string s with some letters turned into digits"""
    #Str -> Str
    returnString = ""
    for char in s:
        returnString = returnString + transformedCharacter(char)
    return returnString

##userString2 = input("Please input a string: ")
##for cha in userString2:
##    print(transformed(cha))


#Lecture Quiz 4A

#Define a function called allInts that takes a tuple of numbers and returns a tuple of integers, replacing any non
#integral values with an integer version


def all_ints(numTuple):
    """This function takes a numTuple and goes through it to set each float to an integer"""
    #Tuple of numbers -> tuples of ints
    blankTuple = ()
    for num in numTuple:
        blankTuple += (int(num),)

    return blankTuple

##tupl = (5, 6.7, 6.2, 7)
##print(all_ints(tupl))

##################

#Using for loops to ask questions
#Function determines if a string has any digits in it

def is_digit(char):
    """This functions takes a char and return a boolean, checking if the char is a number"""
    #char -> Bool

    #the in operator tests whether an object is one of the objects in the given container
    #if the container is a string, in tests substrings
    return char in "0123456789"
    


def has_digits(s):
    """Determines whether s contains any digits"""
    #str -> boolean

    for char in s:
        if is_digit(char):
            return True #if this one character is a digit, don't need to check the rest
    return False #If we get through all the characters and none are digits, then we can return false

print(has_digits("f00bar"))





