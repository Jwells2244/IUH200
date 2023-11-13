def bleep(string, changeChar):
    """This function bleep, takes in two parameters, the first being a string, and the second being a string that holds the
    characters/s that the first string will change into."""
    #String, String -> String
    return (changeChar * len(string))

def minutes(minuteString):
    """This function minutes takes a string called minuteString entered in an h:mm format and returns the amount of minutes
    that are represented in the parameter string"""
    #String -> int
    return int((minuteString[len(minuteString)-2:]))

def hours(hourString):
    """This function hours takes a string called hourString entered in an h:mm format, and returns the amount of hours
    that are represented in the parameter string"""
    #String -> int
    return int((hourString[0: len(hourString)-3]))

def hours_and_minutes(hourAndMinuteString):
    """This function hours_and_minutes takes a string called hourAndMinuteString and returns the amount of hours and
    minutes, seperated by a comma, using the hours and minutes function defined above."""
    #String -> String
    return ("("+ str(hours(hourAndMinuteString)) + ", " + str(minutes(hourAndMinuteString)) + ")")

def flop_flip(flopString):
    """This function flop_flip takes a string called flopString, cuts it in half, puts it in reverse order, and returns that string.
    if the number has an odd number of characters, then the first half should be the shorter one."""
    #String -> String
    firstHalf = flopString[0:int(len(flopString)/2)]
    secondHalf = flopString[int(len(flopString)/2):]
    return secondHalf + firstHalf

def collatz(number):
    """This function collatz takes a number, and checks if it's even or odd with an if else statement. If the number is even, the
    the function will return half of that number, if it's odd the function will return 3 times the number plus 1."""
    #Int -> Int
    if (number % 2 == 0):
        return(number/2)
    else:
        return((number*3)+1)
    



##print(bleep("smurf", "##"))
##print(minutes("105:04"))
##print(hours("105:04"))
##print(hours_and_minutes("2:33"))
##print(flop_flip("nowhere"))
print(collatz(collatz(collatz(collatz(collatz(collatz(10)))))))
