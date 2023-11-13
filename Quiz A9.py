#Quiz 9a
def swap(L, i, j):
    """Swaps the position of 2 items in the list L, based on their indices."""
    #List, int, int -> None
    temp = L[i]
    L[i] = L[j]
    L[j] = temp
