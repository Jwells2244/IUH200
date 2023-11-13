#1A
def is_integral(num):
    """This function takes a floating point number and determines whether or not it represents and integer
    #Num -> Bool"""
    if num % 1 != 0:
        return False
    else:
        return True

#1B
def is_approx_integral(num, precision):
    """Determines whether or not num is close (to the givenprecision) to an integer.
    #Num -> Bool"""
    roundedNum = round(num)
    if ((num+precision) >= roundedNum):
        return True
    elif ((num-precision) >= roundedNum):
        return True
    elif (num % 1 == 0):
        return True
    else:
        return False

#2
def str_to_dollars(dollarString):
    """Takes a string of a money amount, and returns the amount as an integer
    Str -> Num"""
    dollarString = str(dollarString)
    newDollarInt = ""
    potentialDollarSign = dollarString[slice(0,1)]
    if (str(potentialDollarSign) == "$"):
        newDollarInt = float((dollarString[1:]))
    else:
        newDollarInt = float(dollarString)
    if (is_integral(newDollarInt)):
        return int(newDollarInt)
    else:
        if (str(newDollarInt)[-1] == "0"):
            return float(newDollarInt[:-1])
    return newDollarInt

#Q3

GRADE_CUTOFFS = (90, 80, 70, 60)

def pct_to_letter_grade(pct):
    """Returns the letter grade corresponding to the percentage pct, according to the constant GRADE_CUTOFFS
    number -> str"""
    if pct >= GRADE_CUTOFFS[0]:
        return "A"
    elif pct >= GRADE_CUTOFFS[1]:
        return "B"
    elif pct >= GRADE_CUTOFFS[2]:
        return "C"
    elif pct >= GRADE_CUTOFFS[3]:
        return "D"
    else:
        return "F"


#5
#5a

def is_bracketed(string):
    """This functions takes a string and determines whether the first and last character are matching parenthesis or brackets
    str -> Boolean"""
    if string != "":
        if str(string[0]) == "[" and str(string[-1]) == "]":
            return True
        elif str(string[0]) == "(" and str(string[-1]) == ")":
            return True
        else:
            return False
    else:
        return False

#5B

def is_bracketed2(string):
    """this function is identical to is_bracketed, except for it doesn't use if statements, instead doing the comparison on one line
    str -> Boolean"""
    return (string != "") and ((string[0] == "[") and (string[-1] == "]") or (string[0] == "(") and (string[-1] == ")"))
    
