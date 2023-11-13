

def first(L):
    return L[0]

def rest(L):
    return L[1:]


#A list is one of:
# [ ], or
# [x] + L where L is a list


def merged(L1, L2):
    """This function takes two lists and returns a sorted list made up of the elements from L1 and L2 which should
    already be sorted
    list, list -> List"""
    if len(L1) == 0:
        return L2
    elif len(L2) == 0:
        return L1
    else:
        if first(L1) > first(L2):
            return [first(L2)] + merged(L1, rest(L2))
        else:
            return [first(L1)] + merged(L2, rest(L1))
    #Fill later
    return None


def merge_sort(L):
    """Return a sorted copy of L using the merge sort algorithm
    List -> List"""
    if len(L) < 2:
        return L.copy()
    else:
        midpoint = int(len(L)/2)
        left_half = L[:midpoint]
        right_half = L[midpoint:]
        return merged(merge_sort(left_half), merge_sort(right_half))
