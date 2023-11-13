
#A list (of X) is one of:
# [] (the empty list) or
# [x] + L where x is an item of type X and L is another smaller list of X


#Question 1A
def swap(lis, i1, i2):
    """this function takes a list and two indexes, and swaps the items that are at the indexes given
    List, int, int -> None"""
    temp = lis[i1]
    lis[i1] = lis[i2]
    lis[i2] = temp
    
#1B
def insert_sort(list1):
    """This function takes a list and sorts it using the insertion sort method
    List -> None"""
    for i in range(len(list1)):
        if len(list1) == 1:
            break
        for x in range(len(list1)-1, i, -1):
            if not( x-1 < 0):
                if list1[x] < list1[x-1]:
                    swap(list1, x, x-1)

def first(list1):
    """this function takes a list and returns the value of the first index of the list
    List of X -> X"""
    return list1[0]

def rest(list1):
    """this function takes a list and returns a list of every value but the first value
    List of X -> List of X"""
    return list1[1:]



#Question 2B
def insert_into_sorted(list1, item):
    """This function takes an already sorted list, and an item to be added into the appropriate place in the already sorted list
    Returns a copy of the original list
    List, item -> List"""
    if len(list1) == 0:
        return [item]
    elif item < first(list1):
        return [item] + list1
    else:
        return [first(list1)] +  insert_into_sorted(rest(list1), item)

#Question 2C            
def insert_sort_rec(list1):
    """This function takes a list and returns a sorted copy of the list, using insertion sort and recursion
    List -> List"""
    if len(list1) == 1:
        return list1
    else:
        return insert_into_sorted(insert_sort_rec(rest(list1)), first(list1))




#Testing
list2 = [5,6,3,7,3,8]
list3 = [5,1,1,2,3,4,76]
list4 = [5,6,7,2,1,6]

