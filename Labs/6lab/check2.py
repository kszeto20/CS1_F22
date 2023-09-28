'''
Lab 06 
Checkpoint II
'''
row = input("Enter a row: ").strip('\r')
print(row)
row = int(row)

col = input("Enter a column: ").strip('\r')
print(col)
col = int(col)

num = input("Enter a value: ").strip('\r')
print(num)
num = int(num)

bd = [ [ '1', '.', '.', '.', '2', '.', '.', '3', '7'],
       [ '.', '6', '.', '.', '.', '5', '1', '4', '.'],
       [ '.', '5', '.', '.', '.', '.', '.', '2', '9'],
       [ '.', '.', '.', '9', '.', '.', '4', '.', '.'],
       [ '.', '.', '4', '1', '.', '3', '7', '.', '.'],
       [ '.', '.', '1', '.', '.', '4', '.', '.', '.'],
       [ '4', '3', '.', '.', '.', '.', '.', '1', '.'],
       [ '.', '1', '7', '5', '.', '.', '.', '8', '.'],
       [ '2', '8', '.', '.', '4', '.', '.', '.', '6'] ]
'''
print(len(bd))
print(len(bd[0]))
print(bd[0][0])
print(bd[8][8])
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
    
printG(bd)

def ok_to_add(row, col, num):
    add = True
    if (num < 0 or num > 9):
        add = False
    else:
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
        
        if (add):
            bd[row][col] = str(num)
            printG(bd)
    return add

print("Can we add this? {}".format(ok_to_add(row, col, num)))