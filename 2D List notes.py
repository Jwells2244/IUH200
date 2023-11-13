#Example baby sudoku grid:

# 123
# 231
# 312

#The classic way of representing a 2D grid of datapoints like this is as a list of lists

grid1 = [ [1,2,3] , [2,3,1] , [3,1,2] ]
grid2 = [[1,2,3],[2,3,1],[3,1,2]]
grid1 = [[1,2,3],[2,1,1],[3,3,2]]

#A sudoku grid is a square list of integers

#This is an informal data definition. If you include a comment like this in your code, then you can
#use the term grid later on in other comments, including docstrings with purpose statements and signatures

def check_grid_horiz(grid):
    """Determines whether each row in grid has only unique elements"""
    #Grid -> Bool
    for row in grid:
        #Does this row contain any duplicates?
        #If so, return false
        #If not, check the next row
        for num in row:
            if row.count(num) > 1: #Does this number occur more than once in row
                return False          #if so, return False right now
    return True


#to access certain values in a 2d list, use listnam[rownum][item index]

#Quiz 5B

def change_cell(grid, row, col, newVal):
    """This function takes a grid and changes the number at row, col in grid to newVal"""
    #grid, int, int, int -> None
    grid[row][col] = newVal
    return None

def check_grid_vert(grid):
    """This function takes a grid and check to see if every vertical column has only unique elements"""
    #grid -> Bool
    numColumns = len(grid[0])
    numRows = len(grid)
    for col in range(numColumns):
        numSeen = []
        for row in range(numRows):
            num = grid[row][col]
            if num in numSeen:
                return False
            else:
                numSeen.append(num)
    return True

#List comprehensions
#A quick way to build lists out o fother iterable objects kind of a like a mini for loop that builds another list.

