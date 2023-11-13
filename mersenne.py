

def mersenne(n):
    """This function mersenne takes a number n, and then returns 2 to the power of n, minus 1, which
    is called a mersenne number"""
    #num -> num
    return ((2**n)-1)


print("What mersenne numbers do you want to know? Please enter 3 values.")
firstNum = int(input("Number 1: "))
secNum = int(input("Number 2: "))
thirdNum = int(input("Number 3: "))
print("Your mersenne numbers are: " + str(mersenne(firstNum)) + ", " + str(mersenne(secNum)) + ", and " + str(mersenne(thirdNum)))
