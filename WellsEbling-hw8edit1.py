#Question 1
#A *non empty list of numbers* is one of:
#[n] where n is a number, or
#[n]+L where n is a number, and L is a non-empty list of numbers

#[] is a list by definition

def first(L):
    """Returns the first value of a non-empty list
    List-of-Ints -> Integer"""

    return L[0]


def rest(L):
    """Returns all the values in a non-empty list (L) that is not the first value
    List-Of-Ints -> List-Of-Ints"""
    return L[1:]

#Question 1
def minimum(L):
    """Returns the least (in value) in a list of numbers
    Nonempty-List-Of-Numbers -> Integer"""
    if len(L) == 1:
        return L[0]
    elif first(L) > first(rest(L)):
        return minimum(rest(L))
    else:
        return minimum(L[0:1] + rest(rest(L)))
        

##
###Question 2 part a
##def leibmad(curr_n, curr_est, precision):
##    """Returns an estimate of (pi/4) with an error bar smaller than the precision
##    Number, Number, Number -> Number"""
##
##    other_limit = curr_n


###Question 3 part a
def apply_repeatedly(func, start_val, given):
    """This function takes a lambda statement, a starting value, and a given to determine how many times to apply
    the lambda function to the start value"""
    #Function, item of type x, Int -> item of type x
    for i in range(given):
        start_val = func(start_val)
    return start_val



#Question 3 part b
def apply_repeatedly_rec(func, start_val, given):
    """This function does the same thing as apply_repeatedly, using a lambda statement, a starting value, and a
    given to determine how many times to apply the lambda function to the start value, however the major difference
    is that it uses recursion instead of a for loop"""
    #Function, item of type x, Int -> item of type x
    if given == 0:
        return start_val
    else:
        start_val = func(start_val)
        return apply_repeatedly_rec(func, start_val, given-1)


#Question 4 part a
def truncate_str_list(L):
    """Returns a list with the last item in L removed
    Nonempty-List-Of-Strings -> Nonempty-List-Of-Strings"""
    return list(map(lambda l: l[0:-1], L))
    

    
#Question 4 part b
def is_anagram(s1, s2):
    """Determines whether s1 and s2 are anagarams of each other
    String -> Boolean"""

    if len(s1) == len(s2) and sorted(s1.casefold()) == sorted(s2.casefold()):
        return True
    else:
        return False


    
def filter_anagrams(L, target_s):
    """Returns a list fo words from L that are anagrams of target_s
    List, String -> List"""

    return list(filter(lambda s: is_anagram(s, target_s), L))


    

