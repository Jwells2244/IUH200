

def f1(n):
    return f1(n)

def f2(n):
    print(n)
    return f2(n-1)

def f3(n):
    if n == 0:
        return 5
    else:
        return f3(n-1)

def f4(n):
    if n == 0:
        return 5
    else:
        return f4(n-1)*2

#Python runs this, up until a certain point where you are given a recursion error

#pickling is a way to go through every python object and store every value


#n! (n factorial) = 1*2...n

#A natural number is a non-negative integer
#A natural number is any number >= 0
#A natural number n is one of:
# 0, or                     <- Base case of the recursive definition
# n+1 where n is a natural number           <- recursive case of the definition

def factorial(n):
    """returns n factorial"""
    #natural-number -> natural-number
    if n == 0:                  #Base case of the recursive function
        #do something simple
        return 1
    else:                   #Recursive case
        return factorial(n-1) * n


#If you know factorial of n-1, how can you use that to calculate factorial n
#If you know 1*2....*(n-1)
#1*2...*n = (1*2...*(n-1))*n
#factorial(n) = factorial(n-1)*n


#lecture quiz 7B
def gauss(n):
    """Returns the sum of all integers from 0 up to n (inclusive)."""
    #Natural number -> natural number
    if n == 0:
        return 0
    else:
        return gauss(n-1)+n

#fibbonacci sequence:
# 1, 1, 2, 3, 5, 8, 13: to get the next number you add the last 2
#fib(n) = fib(n-1) + fib(n-2)
#fib(0) = 1
#fib(1) = 1

def fib(n):
    """Returns the nth fibonacci number"""
    #natural-number -> natural-number
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return fib(n-1) + fib(n-2)

#A binary number tree is one of:
# a number, or
# (B1, B2), where B1 and B2 are BNTs

#We can represent a tree like this

bnt1 = ( ( 5 , (7 , ( 6,1 ) ) ) , ( 4 , (2,8)))

def num_leaves(tree):
    """This function determines the number of leaves in the BNT"""
    # bnt -> int
    if isinstance(tree, int):
        #base case
        return 1
    else:
        #recursive case. We want to call num_leaves on both of the smaller components of tree.
        # tree must be a tuple mof the form (*,*). The two parts of the tree are tree[0] and tree[1]
        #Since this is recursion, we're going to take those two parts and run them through the num_leaves function
        #num_leaves(tree[0]) and num_leaves(tree[1])

        #How can I use this information (the number of the leaves in left half of the tree, and the number of leaves
        # in the right half of tree, to calculate the number of leaves in the whole tree
        return num_leaves(tree[0]) + num_leaves(tree[1])
    

