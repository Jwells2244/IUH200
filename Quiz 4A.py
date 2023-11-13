
#Jonathan and George


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

tupl = (5, 6.7, 6.2, 7)
print(all_ints(tupl))


#Define a function called all_digits that returns true when passed a string consisting of only digots and False when
#passed a string that has any non digits

def all_digits(string):
    """This function takes a string and returns true if it only has digits
      str-->boolean"""

    for char in string:
        if not (char in "123456789"):
            return False
    return True

testString ="23455"
badTestString = "234HG56"
print(all_digits(testString))
print(all_digits(badTestString))
