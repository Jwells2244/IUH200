##Question 1a.
def collatz(number):
    """This function takes a number and checks whether it's an even number of an
    odd number. If it's an even number, it divides the number by 2. If it's an
    odd number, it takes the number times 3 and adds one.
    Integer -> Integer"""
    if number%2 == 0:
        return int(number/2)
    else:
        return int(((number*3)+1))


##Question 2a. 
def num_classify1(number):
    """this function will return the word negative if it is less than zero and
if it is exactly zero it will return the world zero and if the number is greater
than zero and less than 100 it will return the word small and and if the number
is 100 or larger it will return the word big
    Integer-> String"""
    if number < 0:
        return "negative"
    if number == 0:
        return "zero"
    if number <= 99:
        return "small"
    if number >= 100:
        return "big"


##Question 2b
def num_classify2a(number):
    """this function will return the word negative if it is less than zero and
if it is exactly zero it will return the word zero and if the number is greater
than zero and less than 100 it will return the word small and if the number
is 100 or larger it will return the word big
    Integer-> String"""
    if number < 0:
        return print("negative")
    else:
        if number == 0:
            return print("zero")
    if number <= 99:
            return print("small")
    else:
            return print("big")
    

##question 2c.

def num_classify3(number):
    """this function will return the word negative if it is less than zero and
if it is exactly zero it will return the word zero and if the number is greater
than zero and less than 100 it will return the word "small" and and if the number
is 100 or larger it will return the word big
    Integer-> String"""  
    if number < 0:
        return "negative"
    elif number == 0:
        return "zero"
    elif number <= 99:
        return "small"
    else:
        return "big"
    

















