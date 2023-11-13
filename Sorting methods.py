#Sorting algorithms
#Quicksort is an *in-place* sorting algorithm
#Which means that it never makes a copy of the list,. It works by swapping items in the list itself, and
#only needs a small amount of memory to work.
#Quicksort is designed to work on arrays, where changing values is cheap, but you cant really add or remove
#values from an array

#Merge sort is a sorting algorithm that produces a sorted copy of the original list, which means that it does
#use up extra memory than quicksort or other in-place sorting algorithms.
#Merge sort is more at home in functional programming paradigm, and uses recursion based on first() and rest()
#functions to produce a sorted copy of a list

#Quiz 9a
def swap(L, i, j):
    """Swaps the position of 2 items in the list L, based on their indices."""
    #List, int, int -> None
    temp = L[i]
    L[i] = L[j]
    L[j] = temp

def quicksort(L, lo_idx, hi_idx):
    """Sorts everything in L from lo_idx to hi_idx (using the quicksort algorithm) from smallest to largest uisng <"""
    #List, int, int -> None
    if hi_idx - lo_idx < 1:
        return None
    else:
        #Find a pivot and do the partition
        pivot_idx = partition(L, lo_idx, hi_idx)
        
        quicksort(L, lo_idx, pivot_idx-1) #sort the left part of the list
        quicksort(L, pivot_idx+1, hi_idx) #sort the right part of the list

def partition(L, lo_idx, hi_idx):
    """Partition L so that the pivot value, intitially the last value in L is in the middle, with all smaller values to the left
    and all larger values to the right. Returns the new index of the pivot"""
    #List, int, int -> int
    pivot_value = L[hi_idx]
    pivot_idx = lo_idx-1

    for j in range(lo_idx, hi_idx+1):
        if L[j] <= pivot_value:
            pivot_idx += 1
            swap(L, pivot_idx, j)
    return pivot_idx

from random import shuffle

L1 = list(range(10))
shuffle(L1)
