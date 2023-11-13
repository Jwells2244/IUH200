import math
#Lab 2
def cube(num):
    """This function takes a number and returns the number cubed, or put to
       the power of 3.
       Number -> Number"""
    return num**3

def mutiplicate(the_string, multiple):
    """This function takes a string for the first argument and an integer for the
    second. It multiplies the string by the int, and returns the multiplied
    string"
    String, Int -> String"""
    return(the_string*multiple)


def suffix(the_string, point):
    """This function takes a string and an integer, and returns the integer
    amount of characters starting from the last character and going to the
    front.
    String, Integer -> String"""
    return the_string[len(the_string)-point:]

def triplicate(the_string):
    """In this function, the function takes in the input variable as a string,
    and then returns that string duplicated 2, so that the return string is three
    times what the original string was
    String->String"""
    return(the_string*3)

def avg(num1, num2, num3, num4):
    """In this function avg, the function takes four parameters, and then finds
    and returns the average of the four numbers
    Num, Num, Num, Num -> Num"""
    return(float((num1+num2+num3+num4)/4))


def pythag(opposite, adjacent):
    """This function takes the adjacent and opposite side lengths of a right
    triangle and returns the lenght of the hypotenuse
    Num, Num -> Num"""
    return math.sqrt(opposite**2 + adjacent**2)

def findingDisplacement(initialV, a, t):
    """The function takes acceleration, time, and inital velocity and returns
    the total displacement over the period
    Num, Num, Num -> Num"""
    return float((initialV*t)+(0.5*a*(t**2)))


print(findingDisplacement(2,1,6))


print(avg(1,2,3,4))
print(triplicate("na "))
print(pythag(5,12))

print(suffix("nuclear",5))
