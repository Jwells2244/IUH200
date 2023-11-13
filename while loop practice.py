#Simulation of a conversation with a 4-year-old

##print("This is a simulation of a conversation with a 4-year-old child. You go first")
##
##user_input = input("> ")
##
##while user_input != "because":
##    print("Why?")
##    user_input = input("> ")
##
##print("Okay")

#This is case sensitive, but it doesn't really need to be

#print("This is a simulation of a conversation with a 4-year-old child. You go first")

##user_input = input("> ")
##
##while user_input != "because" or user_input != "Because":
##    print("Why?")
##    user_input = input("> ")
##
##print("Okay")

#This is the wrong condition

##print("This is a simulation of a conversation with a 4-year-old child. You go first")
##
####user_input = input("> ")
####
####while user_input != "because" and user_input != "Because":
####    print("Why?")
####    user_input = input("> ")
####
####print("Okay")
##
##user_input = input("> ")
##
##while not (user_input == "because" and user_input == "Because"):
##    print("Why?")
##    user_input = input("> ")
##
##print("Okay")
##
##


#####Methods
#A method is a kind of function that's attached to an object of a particular type.
#Today we will mostly talk about string methods

#Normal function call syntax
#functionname(argument1, arguemnt2...)

#Method call syntax
#argument1.methodname(other args)

#.upper(), sets a string to uppercase letters
#isupper() checks to see if the word is uppercase, islower() checks if word is all lowercase
#.casefold() will lowercase and take other characters such as german characters and uncombine them

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


print("This script collects a bunch of number and displays the product of them")


total = 1

while True:
    print("Please enter a number. Enter done when finished: ")
    user_input = input();
    if user_input.casefold() == "done":
        break
    if user_input.isdigit():
        total = total * int(user_input)
    else:
        print("I didn't understand that number, please try again: ")
        continue
print("The product of all of the numbers you entered is " + str(total))
    
