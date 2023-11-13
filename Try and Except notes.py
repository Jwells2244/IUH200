#Devin and Jonathan


def get_num_from_user():
    """Repeatedly asks the user to input a number until they give a valid floating point number
    then returns that value"""
    #-> float
    while True:
        print("Please enter a number:")
        user_input = input("> ")
        #check if this is a valid float
        #if so, return float of user input
        #if not, ask for a new number and loop again

        try:
            return float(user_input)
        except ValueError:
            print("Not a valid number, please try again")
    #Done
    return float(user_input) #This is only here to stop formatting tab issues



#Syntax for try-except:
##try:
##    #Block of code that may throw an error
##except ErrorType, ErrorType2, ...:
##    #Code to carry out if that exception of type 1 or 2 occurs
##except ErrorType3:
##    #Code to carry out if exception 3 occurs



#########
#If we wanted to store information about all of the items at a restaurant and their prices in a single variable
#Option 1: A list of two-item lists (each storing a string and a float)

#Option 2: A tuple of two-item tuples (string, float)
#Probably not a good use of tuples, since we'll want to add and remove and change things periodically

#Option 3: A set of two-item lists or tuples
#Not a bad option

#For now, let's do option 1:
#A pricelist is a list of two item lists, a string and a float, representing the name and price of each item

pricelist1 = [["fries",3.99],["burger",5.99],["milkshake",3.49]]



#Quiz 6A
##def get_price(itemName, pricelist):
##    """Returns the price of itemName from the pricelist"""
##    #String, Pricelist -> Float
##    counter = 0
##    while counter < len(pricelist):
##        if pricelist[counter][0] == itemName:
##            return pricelist[counter][1]
##        counter += 1
##    #What should happen if this function is passed a string that doesn't appear as an item name
##    #Option 1
##    #Return some kind of default value like 0
##    #Option 1a: Return some kind of default value of the right type, that could never come up normally like -1
##    #Option 2: Raise an error ourselves. (More modern) so anyone who uses our function could try and catch the error
##    
##    


def get_price(itemName, pricelist):
    """Returns the price of itemName from the pricelist"""
    #String, Pricelist -> Float
    counter = 0
    while counter < len(pricelist):
        if pricelist[counter][0] == itemName:
            return pricelist[counter][1]
        counter += 1
    #If we don't find the item with the given name
    raise ValueError("No item with the name "+ itemName)


######
#What we really want is not a list of two-item lists, but a list-like thing where we can look up items not by their
#position but by some keyword, (in this case, the item name)

#In python this is called a *dictionary*, abbreviated dict.

#A dictionary is an iterable object (not a sequence), where we can look things up not by index, but by some sort
#of key (in this case, a string would make a useful key


#A pricedict is a dictionary with strings(item names) as keys and floats (prices) as values

pricedict1 = {"fries":3.99, "burger":5.99, "milkshake":3.49}

