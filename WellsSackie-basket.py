#Basket Problem

#Question 6


print("Add as many items to the basket as you want.  When you’re done, enter’nothing’.")

userInp = input("What do you want to put in the basket now: ")

basket = ()
counter = 0

while userInp != "nothing":
    print("Okay.")
    counter += 1
    basket += (("Item " + str(counter) + ":   " + userInp),)
    userInp = input("What do you want to put in the basket now: ")

print("There are " + str(counter) + " items in the basket")
for string in basket:
    print(string)
