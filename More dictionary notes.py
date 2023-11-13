
#A pricelist is a dictionary whose keys are string(item names) and values are floats(prices in dollars)

pl = {"fries":3.99, "burger":5.49, "milkshake":3.89}


#Quiz 6B

def change_name(priceList, oldName, newName):
    """This function changes the name of the thing called oldname to newname in the given pricelist"""
    #pricelist, string, string -> None
    priceList[newName] = pricedict[oldName]
    del priceList[oldName]


def display_menu(priceList):
    """Print a menu of all items in pricedict, with their prices"""
    #Pricedict -> None
    for key in priceList:
        print(key + ": $" + str(priceList[key]))
    return None


###########
#Working with files in python.

#There's a built in function called open that opens an existing file or creates a new one,
#so we can work with that file

# open(filename)
# to read = open(filename).read()

#The open function creates an object (a file object of type TextIOWrapper) that has tools for accessing
# the given file
# File objects have a method called .read, and if you call .read with no arguments, it will read from the
#current pointer in the fule all the way until the end of the file and return the contents as a text
# string. And afterwards, the pointer has moved to the end of the file

#the parenthesis in read can be assigned a certain character length to read and move the pointer to that amount

#the method .readline returns the next line of text including the line break character

#.tell returns the current position of the pointer

#.seek takes an integer and moves the pointer to that point in the file

#When theres a problem working with a file, an OSError of some type will get raised. There are many subtypes
# of OSError including: FileNotFoundError and FileFoundError, IsADirectory, PermissionError

#In this class, anytime we work with a file, we are going to include it in a try, except block and catch any OS errors


###
#this script will ask the user for a file name, open the corresponding file, and print its contents one line at a time

##fileName = input("Please enter a filename: ")
##try:
##    file = open(fileName)
##    while True:
##        line = file.readline()
##        if line == "":
##            break
##        else:
##            print(line)
##    file.close()
##except OSError:
##    print("Problem")


#Modify this script so when there's a problem with this file it asks the user to keep trying until it works

while True:
    fileName = input("Please enter a filename: ")
    try:
        file = open(fileName)
        while True:
            line = file.readline()
            if line == "":
                break
            else:
                print(line)
        file.close()
        break
    except OSError:
        print("Problem")

#Python keywords with and as are used to help clean up the text of a python file. Python 3 has the with as keywords
#which you can use whenever you are creating an object that needs to be cleaned up when you're done with it.

with <command to create the object> as <variable to store object>:
    #commands to carry out involving the object
#stuff that happens when you're done with the object


