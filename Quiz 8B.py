#Quiz 8 B

#Jonathan Wells and Mia

def rest(L):
    """Returns a list of everything but the first item in L"""
    #Non empty list -> List
    newList = []
    for val in L:
        if val != L[0]:
            newList.append(val)
    return newList
