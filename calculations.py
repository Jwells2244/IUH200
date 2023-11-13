#Calculations.py


#Question 4

userInp = input("Please enter a number (enter done when done): ")
total = 0
counter = 0
largest = 0

while userInp != "done":
    total += float(userInp)
    counter += 1
    if counter == 1:
        largest = float(userInp)
    else:
        if largest <  float(userInp):
            largest = float(userInp)
    userInp = input("Please enter a number (enter done when done): ")


print("You have entered " + str(counter) + " numbers.")
print("The sum of all of the numbers is " + str(total))
print("The average of all numbers is " + str((total/counter)))
print("The largest number entered is " + str(largest))
    
    
