'''
Homework V
Part II
'''
# imports
import hw5_util as h5

# functions

def gridPrint(grid):
    for i in range(len(grid)):
        print('', end = '  ')
        for j in range(len(grid[i])):
            if (j != (len(grid[i]) - 1)):
                lenOW = len(str(grid[i][j]))
                if (lenOW == 1):
                    print(' {}  '.format(grid[i][j]), end = '')
                elif (lenOW == 2):
                    print('{}  '.format(grid[i][j]), end = '')
                else:
                    print('{} '.format(grid[i][j]), end = '')
            else:
                lenOW = len(str(grid[i][j]))
                if (lenOW == 1):
                    print(' {}'.format(grid[i][j]), end = '')
                else:
                    print('{}'.format(grid[i][j]), end = '')
            '''
            print(' ' * (max(0, 2 - len(str(grid[i][j])))), grid[i][j], end = '')
            print(' ' * (1 + min(1, (2 - len(str(grid[i][j]))), )), end = '')
            '''
        print()

def get_nbrs(row, column, maxR, maxL):
    r = row
    c = column
    neighbors = []
    
    if (r == 0):
        if (c == 0):
            neighbors.append([r, c + 1])
        elif (c == maxL - 1):
            neighbors.append([r, c - 1])
        else:
            neighbors.append([r, c - 1])
            neighbors.append([r, c + 1])
        neighbors.append([r + 1, c])
    elif (r == maxR - 1):
        neighbors.append([r - 1, c])
        if (c == 0):
            neighbors.append([r, c + 1])
        elif (c == maxL - 1):
            neighbors.append([r, c - 1])
        else:
            neighbors.append([r, c - 1])
            neighbors.append([r, c + 1])
    else:
        neighbors.append([r - 1, c])
        if (c == 0):
            neighbors.append([r, c + 1])
        elif (c == maxL - 1):
            neighbors.append([r, c - 1])           
        else:
            neighbors.append([r, c - 1])
            neighbors.append([r, c + 1])
        neighbors.append([r + 1, c])
    return neighbors
                
def isNei(startr, startc, endr, endc):
    if (startr == endr):
        #print("Same row", end = '\t')
        if (startc + 1 != endc and startc - 1 != endc):
            #print("Can't step this col", end = '\t')
            return -1
    elif (startc == endc):
        #print("Same col", end = '\t')
        if (startr + 1 != endr and startr - 1 != endr):
            #print("Can't step this row", end = '\t')
            return -1
    elif (startr != endr and startc != endc):
        return -1
    else:
        return 1
    
def stepChange(grid, r1, c1, r2, c2):
    return grid[r2][c2] - grid[r1][c1]
    
def findMax(grid):
    maxi = grid[0][0]
    maxR = 0
    maxC = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if (grid[i][j] > maxi):
                maxR = i
                maxC = j
                maxi = grid[i][j]
    print('global max: ({}, {}) {}'.format(maxR, maxC, maxi))
    return (maxR, maxC, maxi)

def sStep(r, c, gridN, maxS):
    neigh = get_nbrs(r, c, len(gridN), len(gridN[0]))
    #print("These are the neighbors", neigh)
    maxD = -1
    nRow = 0
    nCol = 0
    for i in range(len(neigh)):
        rN = neigh[i][0]
        cN = neigh[i][1]
        #print("Checking ", rN, cN, sep = ' ')
        #print("This is the value ", gridN[rN][cN])
        #print("Curr value: ", maxD)
        if (gridN[rN][cN] > gridN[r][c]):
            #print("in here")
            if (gridN[rN][cN] > maxD and (gridN[rN][cN] - gridN[r][c] <= maxS)):
                maxD = gridN[rN][cN]
                nRow = rN
                nCol = cN
    if maxD != -1:
        #print(nRow, nCol, sep = ',', end = ' ')
        return (nRow, nCol)
    else:
        return maxD
    
def steepP(r, c, gridN, maxS):
    row = r
    col = c
    path = []
    stopper = 1
    while (stopper != -1):
        nextS = sStep(row, col, gridN, maxS)
        if (nextS != -1):
            path.append(nextS)
            row, col = nextS
        else:
            stopper = -1
    return path

def gStep(r, c, gridN, maxS):
    neigh = get_nbrs(r, c, len(gridN), len(gridN[0]))
    #print("These are the neighbors", neigh)
    minD = 1000
    nRow = 0
    nCol = 0
    for i in range(len(neigh)):
        rN = neigh[i][0]
        cN = neigh[i][1]
        #print("Checking ", rN, cN, sep = ' ')
        #print("This is the value ", gridN[rN][cN])
        #print("Curr value: ", maxD)
        if (gridN[rN][cN] > gridN[r][c]):
            #print("in here")
            if (gridN[rN][cN] < minD and (gridN[rN][cN] - gridN[r][c] <= maxS)):
                minD = gridN[rN][cN]
                nRow = rN
                nCol = cN
    if minD != 1000:
        #print(nRow, nCol, sep = ',', end = ' ')
        return (nRow, nCol)
    else:
        return minD

def gradP(r, c, gridN, maxS):
    row = r
    col = c
    path = []
    stopper = 1
    while (stopper != -1):
        nextS = gStep(row, col, gridN, maxS)
        if (nextS != 1000):
            path.append(nextS)
            row, col = nextS
        else:
            stopper = -1
    return path


def localMax(r, c, gridN, maxS):
    neigh = get_nbrs(r, c, len(gridN), len(gridN[0]))
    #print("These are the neighbors", neigh)
    maxD = 1
    for i in range(len(neigh)):
        rN = neigh[i][0]
        cN = neigh[i][1]
        #print("Checking ", rN, cN, sep = ' ')
        #print("This is the value ", gridN[rN][cN])
        #print("Curr value: ", maxD)
        if (gridN[r][c] < gridN[rN][cN]):
            maxD = -1
    
    return maxD


while (1):
    n = input("Enter a grid index less than or equal to 3 (0 to end): ").strip('\r')
    print(n)
    n = int(n)
    if (n > 0 and n <= h5.num_grids()):
        break

maxS = input('Enter the maximum step height: ')
print(maxS)
maxS = int(maxS)

toPrint = input("Should the path grid be printed (Y or N): ").strip('\r')
print(toPrint)
    
gridN = h5.get_grid(n)
print("Grid has {} rows and {} columns".format(len(gridN), len(gridN[0])))
maxInfo = findMax(gridN)

gridS = h5.get_start_locations(n)
#print(gridS)

for grid in gridS:
    print('===')
    stepPath = steepP(grid[0], grid[1], gridN, maxS)
    print('steepest path')
    print('({}, {}) '.format(grid[0], grid[1]), end = '')
    for i in range(len(stepPath)):
        if (i % 4 == 0 and i != 0):
            print()
        print(stepPath[i], end = ' ')
    print()
    # max check
    if (stepPath[len(stepPath) - 1][0] == maxInfo[0] and stepPath[len(stepPath) - 1][1] == maxInfo[1]):
        print("global maximum")
    elif (localMax(stepPath[len(stepPath) - 1][0], stepPath[len(stepPath) - 1][1], gridN, maxS) == 1):
        print("local maximum")
    else: 
        print('no maximum')
    print('...')
    print('most gradual path')
    gradPath = gradP(grid[0], grid[1], gridN, maxS)
    print('({}, {}) '.format(grid[0], grid[1]), end = '')
    for i in range(len(gradPath)):
        if (i % 4 == 0 and i != 0):
            print()
        print(gradPath[i], end = ' ')
    print()
    # max check
    if (gradPath[len(gradPath) - 1][0] == maxInfo[0] and gradPath[len(gradPath) - 1][1] == maxInfo[1]):
        print("global maximum")
    elif (localMax(gradPath[len(gradPath) - 1][0], gradPath[len(gradPath) - 1][1], gridN, maxS) == 1):
        print("local maximum")
    else: 
        print('no maximum')
# for each start 
    # find steep + print
    # print("...")
    # find grad + print
    