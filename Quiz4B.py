#Jonathan Wells and George



#Quiz 4B
#Find a way to get a version of a string with all question marks removed
#Use the replace() method

#Define a function that takes a string to be cleaned and a string containing all the character you want removed
#from the string and that returns a version of the string with all of those characters removed

def clean_out(string, chars):
    """this function takes a string containing characters and another string of characters, and gets rid of any instances of
    one of the characters in the original string"""
    #Str+Str -> Str
    newString = string
    for char in newString:
        if char in chars:
            newString = newString.replace(char, "")
    return newString
