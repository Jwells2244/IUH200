def mersenne(n):
    return (n**2)-1

def frak(string, string1):
    returnString = ""
    for i in string:
        returnString += string1
    return returnString

def hours(string):
    returnS = ""
    for i in string:
        if i == ";":
            break
        else:
            returnS += i
    return int(returnS)

def collatz(num):
    if num % 2 == 0:
        return num/2
    else:
        return (num*3)+1

def is_integral(num):
    if int(num) == 0:
        return False
    else:
        return True

def is_approx_integral(num, precision):
    if abs(num + precision) == abs(int(num) + 1):
        return True
    else:
        return False

def lower_all(list1):
    for i in range(len(list1)):
        list1[i] = list1[i].lower()
    return list1

def all_positive(list1):
    for i in list1:
        if i < 0:
            return False
    return True

def inverses(list1):
    for i in list1:
        list1[i] = 1 / list1[i]
    return list1

def 

            
