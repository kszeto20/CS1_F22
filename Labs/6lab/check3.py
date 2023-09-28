'''
Lab 06 
Checkpoint III
'''

import lab06_util as l6

fName = input("Enter the filename with the board: ").strip('\r')


'''
ask user file name
read board from file
while (board is not solved according to verify_board):
ask user for input to the puzzle
if ok_to_add
add value
print the board
'''



def printG(bd):
    group = 0
    upTo = 1
    print('-' * 25)
    for i in range(9):
        if (group % 3 == 0 and group != 0):
            print('-' * 25)
            group = 0
        print('| ', end = '')
        group += 1
        for j in range(9):
            if (bd[i][j] == 0):
                print('. ', end = '')
            else:
                print(str(bd[i][j]), end = ' ' )
            if (upTo == 9):
                print('| ', end = '')
                print()
                upTo = 0
            elif (upTo % 3 == 0):
                print('| ', end = '')        
            upTo += 1
    print('-' * 25)

def verify_board(bd):
    for i in range(9):
        for j in range(9):
            if (bd[i][j] == '.'):
                return False
            else:
                checkNum = int(bd[i][j])
                bd[i][j] = '.'
                add = ok_to_add(i, j, checkNum)
                if (add):
                    bd[i][j] = checkNum
                else:
                    return False
    
    return True
                
def ok_to_add(row, col, num):
    add = True
    if (num < 0 or num > 9):
        add = False
    else:
        if bd[row][col] != '.':
            return False
            
        for i in range(9):
            if (bd[row][i] != '.'):
                if int(bd[row][i]) == num:
                    add = False
            if (bd[i][col] != '.'):
                if int(bd[i][col]) == num:
                    add = False
    
        
        nR = row // 3 * 3
        nC = col // 3 * 3
        for i in range(nR, nR + 3, 1):
            for j in range(nC, nC + 3, 1):
                if (bd[i][j] != '.'):
                    if int(bd[i][j]) == num:
                        add = False
                        
    return add

print(fName)
bd = l6.read_sudoku(fName)

printG(bd)

while (verify_board(bd) == False):
    row = input("Enter a row: ").strip('\r')
    print(row)
    row = int(row)

    col = input("Enter a column: ").strip('\r')
    print(col)
    col = int(col)

    num = input("Enter a value: ").strip('\r')
    print(num)
    num = int(num)
    
    if (ok_to_add(row, col, num)):
        bd[row][col] = str(num)
        printG(bd)
        