
#1
def digit_sum(string):
    """This function takes a string and returns the sum of all of the numbers contained within the string"""
    #Str -> Int
    total = 0
    for char in string:
        if char in "0123456789":
            total += int(char)
    return total
            



#2
def count_negative(numTuple):
    """This function takes a tuple and returns an integer representing the amount of negative values the
    tuple holds"""
    #Tuple -> Int
    counter = 0
    for value in numTuple:
        if value <0:
            counter += 1
    return counter


#3
def consecutive_sum(startVal, endVal):
    """This function takes a start and end value, and returns the sum of every number between the start and end
    using the range function."""
    # Int, Int -> Int
    totalSum = 0
    for num in range(startVal, endVal+1):
        totalSum += num
    return totalSum




    
