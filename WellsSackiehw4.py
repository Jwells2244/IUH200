
#1A
def has_more_bucks(string1, string2):
    """This function takes two strings, and determines which string has more dollar signs in it"""
    # string, string -> Boolean
    count1 = 0
    count2 = 0
    for char in string1:
        if char == "$":
            count1 += 1
    for char1 in string2:
        if char1 == "$":
            count2 +=  1
    if count1 > count2:
        return True
    else:
        return False

#1B
def has_more_bucks2(string1, string2):
    """This function is like has_more_bucks, in which it takes two strings and determines which string
    has more dollar signs in it, but this time it uses string methods"""
    #String, String -> Boolean
    return string1.count("$") > string2.count("$")

#2
def longest(stringTuple):
    """This function takes a tuple of strings and returns the longest string in the tuple"""
    #Tuple of strings -> String
    longestString = stringTuple[0]
    for strin in stringTuple:
        if len(strin) > len(longestString):
            longestString = strin
    return longestString

#3A
def escape_URL_char(char):
    """This function takes a string of a single character and determines if it needs to be escaped, and if
    the character needs to be escaped, then it will return what the escape sequence is"""
    #String -> String
    if char == " ":
        return "+"
    elif char == "/":
        return "%2F"
    elif char == "#":
        return "%23"
    elif char == "=":
        return "%3D"
    else:
        return char

#3B
def escape_URL(string):
    """This function takes a string and calls the escape_URL_char function to check if each character is a character
    that needs to be escaped, and then returns the completed string"""
    #String -> String
    returnString = ""
    for char in string:
        returnString = returnString + escape_URL_char(char)
    return returnString

#4A
def is_vowel(character):
    """This function takes a single character string, and returns True if it's a vowel, and False if it's not"""
    #String -> Boolean
    if character.upper() == "A":
        return True
    elif character.upper() == "E":
        return True
    elif character.upper() == "I":
        return True
    elif character.upper() == "O":
        return True
    elif character.upper() == "U":
        return True
    else:
        return False

#4B
def has_vowel(string):
    """This function takes a string, and goes through each character and checks if it is a vowel using the function
    is_vowel. If a vowel is contained in the string return True, else False"""
    #String -> Boolean
    for char in string:
        if is_vowel(char):
            return True
    return False

#4C
def all_vowels(string):
    """This function takes a string and goes through each character to check if every single character is a vowel
    using the function is_vowel, and returns true if every charater is a vowel"""
    #String ->Boolean
    allVowels = True
    for char in string:
        if is_vowel(char) == False:
            allVowels = False
    return allVowels

#5
def all_odd(numTuple):
    """This function takes a tuple of integers and checks to see if every number is odd, returning true if so,
    and false if not"""
    #Integer Tuple -> Boolean
    allOdds = True
    for val in numTuple:
        if val % 2 == 0:
            allOdds = False
    return allOdds


#7

#Old Count Negative

##def count_negative(numTuple):
##    """This function takes a tuple and returns an integer representing the amount of negative values the
##    tuple holds"""
##    #Tuple -> Int
##    counter = 0
##    for value in numTuple:
##        if value <0:
##            counter += 1
##    return counter

def count_negative2(numTuple):
    """this function takes a tuple and returns an integer representing the amount of negative values the
    tuple holds, using a while loop"""
    #Tuple of nums -> Int
    counter = 0
    index = 0
    while index < len(numTuple):
        if numTuple[index] < 0:
            counter += 1
        index += 1
    return counter
        
    




    
