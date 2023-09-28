'''
Homework V
Part I
'''
# imports
import hw5_util as h5

# functions

# to print the mountain map 
def gridPrint(grid):
    for i in range(len(grid)):
        print('', end = '  ') # original two spaces at the beginning of each new line
        for j in range(len(grid[i])):
            # if not at the end of the row
            if (j != (len(grid[i]) - 1)):
                lenOW = len(str(grid[i][j]))
                # if height is one digit
                if (lenOW == 1):
                    print(' {}  '.format(grid[i][j]), end = '')
                # if height is two digits
                elif (lenOW == 2):
                    print('{}  '.format(grid[i][j]), end = '')
                # if height is three digits
                else:
                    print('{} '.format(grid[i][j]), end = '')
            # if at the end of row
            else:
                lenOW = len(str(grid[i][j]))
                # if height is one digit
                if (lenOW == 1):
                    print(' {}'.format(grid[i][j]), end = '')
                # else if height is two or three digits
                else:
                    print('{}'.format(grid[i][j]), end = '')
        print() # new line for next row

# get neighbors of a position
def get_nbrs(row, column, maxR, maxL):
    r = row
    c = column
    neighbors = [] # list of neighbors of the given position
    
    # order of neighbors = up, right, left, down
    
    # first row
    if (r == 0):
        # top left corner - only has right neighbor 
        if (c == 0):
            neighbors += [r, c + 1]
        # top right corner - only has left neighbor
        elif (c == maxL - 1):
            neighbors += [r, c - 1]
        # middle - has left and right neighbor
        else:
            neighbors += [r, c - 1]
            neighbors += [r, c + 1]
        neighbors += [r + 1, c] # if first row there will always be one row below
    
    # last row
    elif (r == maxR - 1):
        neighbors += [r - 1, c] # if last row there will always be one row above
        # bottom left corner - only has right neighbor
        if (c == 0):
            neighbors += [r, c + 1]
        # bottom right corner - only has left neighbor
        elif (c == maxL - 1):
            neighbors += [r, c - 1]
        # middle - has left and right neighbor
        else:
            neighbors += [r, c - 1]
            neighbors += [r, c + 1]
    # middle rows
    else:
        # if in the middle there will always be a top row
        neighbors += [r - 1, c]
        # left border - only has right neighbors
        if (c == 0):
            neighbors += [r, c + 1]
        # right border  - only has left neighbors
        elif (c == maxL - 1):
            neighbors += [r, c - 1]
        # middle - has left and right neighbors            
        else:
            neighbors += [r, c - 1]
            neighbors += [r, c + 1]
        # if in middle there will always be a bottom row
        neighbors += [r + 1, c]
        
    return neighbors

# checks if two coors (in a path) are actually neighbors 
def isNei(startr, startc, endr, endc):
    # -1 is not valid, 1 is valid
    # if same row
    if (startr == endr):
        # col must be one step to right or to left
        if (startc + 1 != endc and startc - 1 != endc):
            return -1
    # if same col
    elif (startc == endc):
        # row must be one step up or down 
        if (startr + 1 != endr and startr - 1 != endr):
            return -1
    # if they are not even on the same row or col - not valid
    elif (startr != endr and startc != endc):
        return -1
    # all other cases are valid
    else:
        return 1

# how big the step is
def stepChange(grid, r1, c1, r2, c2):
    return grid[r2][c2] - grid[r1][c1]

# Part I output
 
# ask user for grid number (loop until given valid number)
while (1):
    # store input in 'n'
    n = input("Enter a grid index less than or equal to 3 (0 to end): ").strip('\r')
    print(n)
    n = int(n)
    # if valid; break loop
    if (n > 0 and n <= h5.num_grids()):
        break

# get the grid n    
gridN = h5.get_grid(n)

# ask user if they want to print grid
toPrint = input("Should the grid be printed (Y or N): ").strip('\r')
print(toPrint)
if (toPrint.lower() == 'y'):
    print("Grid {}".format(n))
    gridPrint(gridN) # function prints map

# grid dimensions
print("Grid has {} rows and {} columns".format(len(gridN), len(gridN[0])))

# get start locations associated with grid n 
gridS = h5.get_start_locations(n)

# for each start location, print valid neighbors
for grid in gridS:
    print("Neighbors of {}: ".format(grid), end = '')
    neigh = get_nbrs(grid[0], grid[1], len(gridN), len(gridN[0]))
    for i in range(0, len(neigh), 2): # increment by 2 because coordinates are in pairs
        if (i != len(neigh) - 2):
            print('({}, {}) '.format(neigh[i], neigh[i+1]), end = '')
        else:
            print('({}, {})'.format(neigh[i], neigh[i+1]), end = '')
    print() # new line for each new start location
    
# get suggested path
gridP = h5.get_path(n)
invalid = False # is the path valid?

downward = 0 # total change in elevation from down steps
upward = 0 # total change in elevation from up steps

for i in range(len(gridP) - 1):
    # for each pair of coors in the path, if ever invalid, whole path is invalid
    if (isNei(gridP[i][0], gridP[i][1], gridP[i + 1][0], gridP[i+1][1]) == -1):
        print("Path: invalid step from {} to {}".format(gridP[i], gridP[i + 1]))
        invalid = True
    else:
        # find elevation change
        change = stepChange(gridN, gridP[i][0], gridP[i][1], gridP[i + 1][0], gridP[i+1][1])
        # if negative, add magnitude to downward
        if (change < 0):
            downward += (change * -1)
        # else add magnitude to upward
        else:
            upward += change

# as long as path is not invalid; print upward and downward count
if (invalid == False):
    print("Valid path")
    print("Downward {}".format(downward))
    print("Upward {}".format(upward))



    
