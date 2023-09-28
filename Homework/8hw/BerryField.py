# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:25:49 2022

@author: szetok2
"""
'''
Berry Class:
    
init = takes in an list of lists for the board of berries
str = prints out board according

totalBerries = counts the amount of berries on the board
printAll = another print function
grow = grow function to add more berries for each non-zero square
spread = spread berries to zero-berry squares
'''

class BerryField(object):
    
    def __init__(self, bfield):
        self.field = bfield
        self.bTotal = 0
        
    def __str__(self):
        
        inF = ''
        
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if self.field[i][j] == 'B' and self.field[i][j] == "T":
                    inF += "{:>4} ".format('X')
                elif self.field[i][j] == 'B':
                    inF += "{:>4} ".format('B')
                elif self.field[i][j] == "T":
                    inF += "{:>4} ".format('T')
                else:
                    inF += str(self.field[i][j])
                    inF += ' '
            inF += '\n'
                    
        return inF
    
    def totalBerries(self):
        total = 0
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                total += self.field[i][j]
        
        return total
    
    def printAll(self, b, t):
        total = self.totalBerries()
        self.bTotal = total
        
        print('Field has {} berries.'.format(total))
        grid = ''
        
        hasB = False
        hasT = False
        
        for r in range(len(self.field)):
            for c in range(len(self.field[0])):
                for bear in b:
                    if bear.row == r and bear.col == c:
                        hasB = True
                for tour in t:
                    if tour.row == r and tour.col == c:
                        hasT = True
                
                if hasB and hasT:
                    grid += '{:>4}'.format('X')
                elif hasT:
                    grid += '{:>4}'.format('T')
                elif hasB:
                    grid += '{:>4}'.format('B')
                else:
                    grid += '{:>4}'.format(self.field[r][c])
                hasB = False
                hasT = False
            grid += '\n'
            
        return grid
    
    def grow(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                if self.field[i][j] != 'B' and self.field[i][j] != 'T' and self.field[i][j] != 'X':
                    if 1 < self.field[i][j] and self.field[i][j] < 10:
                        self.field[i][j] += 1
                    
    def spread(self):
        for i in range(len(self.field)):
            for j in range(len(self.field[0])):
                #print('in checking')
                if self.field[i][j] == 0:
                    if self.field[i-1][j] == 10 or self.field[i+1][j] == 10 or self.field[i][j+1] == 10 or self.field[i][j+1] == 10 or self.field[i-1][j - 1] == 10 or self.field[i+1][j - 1] == 10 or self.field[i - 1][j+1] == 10 or self.field[i + 1][j+1] == 10:
                        self.field[i][j] += 1

'''
Testing
f = [['T', 0, 10], [5, 'B', 5], [12, 'B', 'B']]

a = BerryField(f)
print(a)
a.spread()
print(a)
a.grow()
print(a)
'''