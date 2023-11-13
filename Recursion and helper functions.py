
def sqrt(num, precision):
    """This function takes a number and calculates the square root of the number, to the given precision value"""
    #Number, number -> Num
    first_guess = num / 2
    return sqrt_helper(num, first_guess, precision)


def sqrt_helper(num, guess, precision):
    """This function calculates the square root of num, starting with the given guess, and ending with the desired
    precision"""
    #Number, Number, Number -> Number
    
    other_limit = num / guess
    current_precision = abs(guess-other_limit)
    new_guess = (guess + other_limit)/2
    
    if current_precision < precision:
        return new_guess
    else:
        return sqrt_helper(num, new_guess, precision)


#default values and keyword arguments for function definitions

def nth_root(num, n=2):
    """Calculates the nth root of num. Defaults to square root."""
    #Number [, positive integer] -> Number
    return num ** (1/n)


#####
#If there isn't an obvious default value, but you want to make one of your arguments optional, use the value of none.
# And inside the function you can test whether the argument is == to None to determine whether or not the optional
# value was included.

def sqrt2(num, precision, guess=None):
    """This function calculates the square root of num, starting with the given guess, and ending with the desired
    precision"""
    #Number, Number [, Number] -> Number
    if guess == None:
        guess = num/2
    other_limit = num / guess
    current_precision = abs(guess-other_limit)
    new_guess = (guess + other_limit)/2
    
    if current_precision < precision:
        return new_guess
    else:
        return sqrt2(num, precision, new_guess)

#We use square brackets around any part of the signature that represents an optional argument

######################

#A *list of x* is one of:
    # [ ]
    # [X]+L, where x is of type x and L is a list of x

#[] is a list by definition
#[1] is a list of ints because it's equal to [1] = [1] + [] and 1 is an int and [] is a list
#[2,1] is a list of ints because [2,1] = [2] + [1] and 2 is an int and [1] is a list of ints

def first(L):
    """Returns the first item in a list"""
    #List of x -> x
    return L[0]

#Quiz 8B

def rest(L):
    """Returns a list of everything but the first item in L"""
    #Non empty list -> List
    newList = []
    for val in L:
        if val != L[0]:
            newList.append(val)
    return newList

def recursive_sum(numList):
    """Returns the sum of all values in numList"""
    #List of nums -> Number
    if numList == []:
        return 0
    else:
        return recursive_sum(rest(numList)) + first(numList)
