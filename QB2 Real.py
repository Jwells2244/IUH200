# Jonathan Wells and Jack Tyndall

#Quiz Q2B
#Take the function that you defined last time to calculate the volume of a box
# and use that to create a script that asks the user to enter in 4 things, a density
# a width, length, and height and then calculate the mass of a block of that size with that density

def volumeOfBox(l, w, h):
    """This function calculates the volume of a box using it's length, width and height
    Number, Number, Number -> Number
    All Arguments should have the same units, and the output is in that unit cubed"""
    return(l*w*h)

lengt = float(input("What is the length of the block(cm): "))
width = float(input("What is the width of the block(cm): "))
height = float(input("What is the height of the block(cm): "))
density = float(input("what is the density of the material (in g/cm^3): "))

print("The block weighs " + str((float(volumeOfBox(lengt, width, height)) * density)) + "g")
