'''
Homework V
Part II
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
            neighbors.append([r, c + 1])
        # top right corner - only has left neighbor
        elif (c == maxL - 1):
            neighbors.append([r, c - 1])
        # middle - has left and right neighbor
        else:
            neighbors.append([r, c - 1])
            neighbors.append([r, c + 1])
        neighbors.append([r + 1, c]) # if first row there will always be one row below
    
    # last row
    elif (r == maxR - 1):
        neighbors.append([r - 1, c])# if last row there will always be one row above
        # bottom left corner - only has right neighbor
        if (c == 0):
            neighbors.append([r, c + 1])
        # bottom right corner - only has left neighbor
        elif (c == maxL - 1):
            neighbors.append([r, c - 1])
        # middle - has left and right neighbor
        else:
            neighbors.append([r, c - 1])
            neighbors.append([r, c + 1])
    # middle rows
    else:
        # if in the middle there will always be a top row
        neighbors.append([r - 1, c])
        # left border - only has right neighbors
        if (c == 0):
            neighbors.append([r, c + 1])
        # right border  - only has left neighbors
        elif (c == maxL - 1):
            neighbors.append([r, c - 1])
        # middle - has left and right neighbors            
        else:
            neighbors.append([r, c - 1])
            neighbors.append([r, c + 1])
        # if in middle there will always be a bottom row
        neighbors.append([r + 1, c])
        
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
                
# find the max elevation of the map
def findMax(grid):
    maxi = grid[0][0] # max value
    maxR = 0 # row cor of max value
    maxC = 0 # col cor of max value
    # loop through whole map
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            # if current value is bigger than max
            if (grid[i][j] > maxi):
                # update the values
                maxR = i
                maxC = j
                maxi = grid[i][j]
    # output
    print('global max: ({}, {}) {}'.format(maxR, maxC, maxi))
    return (maxR, maxC, maxi)

# steepest step (find steepest neighbor of a given coordinate)
def sStep(r, c, gridN, maxS, pathG): # row, col, grid, maxStep size, pathGraph
    neigh = get_nbrs(r, c, len(gridN), len(gridN[0])) # get neighbors
    maxD = -1 # max elevation of neighbors
    nRow = 0 # max step row
    nCol = 0 # max step col
    # loop through each neighbor
    for i in range(len(neigh)):
        rN = neigh[i][0] # row of neighbor to check
        cN = neigh[i][1] # col of neighbor to check
        # if neighbor is greater than given coordinate
        if (gridN[rN][cN] > gridN[r][c]):
            # if elevation is greater than maxD (greatest elevation so far) and (neighbor elevation - curr elevation < maxStep allowed) 
            if (gridN[rN][cN] > maxD and (gridN[rN][cN] - gridN[r][c] <= maxS)):
                # update the values
                maxD = gridN[rN][cN]
                nRow = rN
                nCol = cN
    # as long as neighbor is chosen (-1 signifies none of neighbors satisfy a moveable point)
    if maxD != -1:
        # update path Graph (graph to show how many times each coor has been touched on a path)
        pathG[nRow][nCol] += 1
        # return the chosen next step
        return (nRow, nCol)
    # if no next step, send back -1
    else:
        return maxD

# finding the whole steepest path    
def steepP(r, c, gridN, maxS, pathG): # row, col, grid, maxStep size, pathGraph
    row = r # current row of coor
    col = c # current col of coor
    path = [] # path decided
    stopper = 1 # have we reached the end of possible moves
    
    # while we still have moves
    while (stopper != -1):
        # find the next step with current step
        nextS = sStep(row, col, gridN, maxS, pathG)
        # if not -1, means can move 
        if (nextS != -1):
            # add the coors of the chosen move
            path.append(nextS)
            # update the current spot with chosen coor row and col
            row, col = nextS
        # else, no more moves, loop breaks (stop checking for more moves)
        else:
            stopper = -1
            
    # return the path
    return path

# gradual step (find most gradual neighbor of a given coordinate)
def gStep(r, c, gridN, maxS, pathG):
    neigh = get_nbrs(r, c, len(gridN), len(gridN[0])) # get neighbors
    minD = 1000 # min elevation of neighbors
    nRow = 0 # min step row
    nCol = 0 # min step col
    # loop through each neighbor
    for i in range(len(neigh)):
        rN = neigh[i][0] # row of neighbor to check
        cN = neigh[i][1] # col of neighbor to check
        # if neighbor is less than given coordinate
        if (gridN[rN][cN] > gridN[r][c]):
            # if elevation is less than minD (lowest elevation so far) and difference between neighbor elevation and current corr < maxStep
            if (gridN[rN][cN] < minD and (gridN[rN][cN] - gridN[r][c] <= maxS)):
                # update values
                minD = gridN[rN][cN]
                nRow = rN
                nCol = cN
    # if a move has be decided
    if minD != 1000:
        # update path Graph (graph to show how many times each coor has been touched on a path)
        pathG[nRow][nCol] += 1
        # return chosen next step
        return (nRow, nCol)
    # if no next step return 1000
    else:
        return minD

# finding whole most gradual path 
def gradP(r, c, gridN, maxS, pathG):
    row = r # current row of corr
    col = c # current col of corr
    path = [] # path decided
    stopper = 1 # have we reached the end of possible moves
    while (stopper != -1):
        nextS = gStep(row, col, gridN, maxS, pathG)
        # if not -1, means can move 
        if (nextS != 1000):
            # add the coors of the chosen move
            path.append(nextS)
            # update the current spot with chosen coor row and col
            row, col = nextS
        # else, no more moves, loop breaks (stop checking for more moves)
        else:
            stopper = -1
    # return the path
    return path

# find if the value is at the local max
def localMax(r, c, gridN, maxS):
    # if greater than all neighbors == local max
    # get neighbors
    neigh = get_nbrs(r, c, len(gridN), len(gridN[0]))
    maxD = 1 # 1 signifies true
    for i in range(len(neigh)):
        rN = neigh[i][0] # row of neighbor
        cN = neigh[i][1] # col of neighbor
        # if there is any instance of a neighbor being greater makes it not a local max
        if (gridN[r][c] < gridN[rN][cN]):
            maxD = -1 # -1 signifies false
            
    return maxD

# print the path grid
def pathPrint(grid):
    for i in range(len(grid)):
        # initial space at the begining of each row
        print('', end = '  ')
        for j in range(len(grid[i])):
            # if it is not at the end of the row
            if (j != (len(grid[i]) - 1)):
                # if value is 0
                if (grid[i][j] == 0):
                    print('.', end = '  ')
                # if value is non-zero
                else:
                    print(grid[i][j], end = '  ')
            # if at the end of the row
            else:
                # if value is 0
                if (grid[i][j] == 0):
                    print('.', end = '')
                # if value is non-zero
                else:
                    print(grid[i][j], end = '')
        print() # new line for next row

# Part II output

# get grid from user
while (1):
    n = input("Enter a grid index less than or equal to 3 (0 to end): ").strip('\r')
    print(n)
    n = int(n)
    if (n > 0 and n <= h5.num_grids()):
        break

# get max step height
maxS = input('Enter the maximum step height: ')
print(maxS)
maxS = int(maxS)

toPrint = input("Should the path grid be printed (Y or N): ").strip('\r')
print(toPrint)
printyn = False
if (toPrint.lower() == 'y'):
    printyn = True

# get grid n 
gridN = h5.get_grid(n)

# generate path grid
r, c = len(gridN), len(gridN[0])
pathG = [[0 for y in range(c)] for x in range(r)]

# print dimensions
print("Grid has {} rows and {} columns".format(len(gridN), len(gridN[0])))
# print and store global max information
maxInfo = findMax(gridN)

# get start locations
gridS = h5.get_start_locations(n)

# for each start location
for grid in gridS:
    # update path grid with start location
    pathG[grid[0]][grid[1]] += 2 # +2 because one path for steepest and one for gradual
        
    print('===')
    # find steepest path
    stepPath = steepP(grid[0], grid[1], gridN, maxS, pathG)
    # steepest path for (startRow, startCol)
    print('steepest path')
    print('({}, {}) '.format(grid[0], grid[1]), end = '')
    # print out resulting path
    nLC = 1
    for i in range(len(stepPath)):
        # newline after every fifth term
        if (nLC == 5):
            print()
            nLC = 0
        # print each path step
        print(stepPath[i], end = ' ')
        nLC += 1
    print()
    # max check for steepest
    # if final r,c coors == global max r,c cooors
    if (stepPath[len(stepPath) - 1][0] == maxInfo[0] and stepPath[len(stepPath) - 1][1] == maxInfo[1]):
        print("global maximum")
    # elif if local max
    elif (localMax(stepPath[len(stepPath) - 1][0], stepPath[len(stepPath) - 1][1], gridN, maxS) == 1):
        print("local maximum")
    # else: neither
    else: 
        print('no maximum')
    print('...')
    # find most gradual path
    gradPath = gradP(grid[0], grid[1], gridN, maxS, pathG)
    print('most gradual path')
    print('({}, {}) '.format(grid[0], grid[1]), end = '')
    # print path same way as steepest
    nLC = 1
    for i in range(len(gradPath)):
        if (nLC == 5):
            print()
            nLC = 0
        print(gradPath[i], end = ' ')
        nLC += 1
    print()
    # max check - same as steepest path
    if (gradPath[len(gradPath) - 1][0] == maxInfo[0] and gradPath[len(gradPath) - 1][1] == maxInfo[1]):
        print("global maximum")
    elif (localMax(gradPath[len(gradPath) - 1][0], gradPath[len(gradPath) - 1][1], gridN, maxS) == 1):
        print("local maximum")
    else: 
        print('no maximum')


if (printyn):
    print('===\nPath grid')
    pathPrint(pathG)