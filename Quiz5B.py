
#Jonathan Wells and Prodescu

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
