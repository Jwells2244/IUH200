#Lab 5

#A
def remove_first_zero1(list1):
    """This function takes a list and removes the first 0 that it finds in the list"""
    #List -> None
    inde = 0
    first = False
    for val in list1:
        if (val == 0) and (first == False):
            del list1[inde]
            first = True
        inde += 1

#B
def remove_first_zero2(list2):
    """This function does the same thing as remove_first_zero1, where it removes the first zero that it finds in a list"""
    #List -> None
    if 0 in list2:
        list2.remove(0)

#C
def remove_all_zeros1(list3):
    """This function takes a list and removes all zeros from it"""
    #List -> None
    index = 0
    for val in list3:
        if val == 0:
            del list3[index]
        index += 1
    
#D
def remove_all_zeros2(list4):
    """This function takes a list and removes all zeros from it, similar to remove_all_zeros1"""
    #List -> None
    while 0 in list4:
        list4.remove(0)

#E
def without_zeros(list5):
    """This function takes a list and returns a copy with all of the zeros removed"""
    #List of nums -> List of nums
    copyList = list5
    while 0 in copyList:
        copyList.remove(0)
    return copyList

#2A
def remove_duplicates(list1):
    """This function takes a list and removes any duplicate values in the list"""
    #List -> None
    singlesList = []
    for val in list1:
        if val not in singlesList:
            singlesList.append(val)
    list1[:] = singlesList
    
#2B

def filter_duplicates(list2):
    """This function takes a list and returns a copy of the original list with duplictaes removed"""
    #List -> List
    singlesList = []
    for val in list2:
        if val not in singlesList:
            singlesList.append(val)
    return singlesList


