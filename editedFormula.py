import math
print("This program will calculate the length of the hypotenuse of a right triangle")
units = input("Enter the units that you will enter both numbers in: ")
first = (int(input("Enter the length of the base of the triangle: "))) **2
second = (int(input("Enter the length of the second side of the triangle: ")))**2
print("The hypotenuse of the triangle has the length of: " +
str(math.sqrt(first+second)) + " " + units + ".")
