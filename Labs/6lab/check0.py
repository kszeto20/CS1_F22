'''
Lab 06
Checkpoint 0
'''

# #1
line = ''
for i in range(9):
    line += str(i)
    if (i != 8):
        line += ' '
    
print(line)

# #2

group = 0

upTo = 1
for i in range(9):
    if (group % 3 == 0):
        print()
        group = 0
    group += 1
    for j in range(9):
        print('{},{}'.format(i, j), end = ' ')
        if (upTo == 9):
            print()
            upTo = 0
        elif (upTo % 3 == 0):
            print(" ", end = '')
        
        upTo += 1
        
print()
for i in range(9):
    print('{},{}'.format(2, i), end = ' ')
    
print()
for i in range(9):
    print('{},{}'.format(i, 5), end = ' ')
    
print()
print()
upTo = 1
for i in range(3):
    for j in range(3):
        print('{},{}'.format(i, j), end = ' ')
        if (upTo == 3):
            print()
            upTo = 0
        upTo += 1




