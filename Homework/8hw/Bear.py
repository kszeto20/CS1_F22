# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 15:51:38 2022

@author: szetok2
"""
'''
Bear Class
init = takes in location tuple and direction of motion
str = str for each bear, gives row, column, travel direction, is the bear asleep or not
move = takes care of motion for bear object 
    --> keeps eating and moving until full
    --> stops moving if it is full or encounters a tourist
        --> if encounters a tourist = bear goes to sleep (will wake up after 2 turns)
        
changeCoor = updates coor of bear (regardless of bounds) in corresponding direction

'''

class Bear(object):
    
    def __init__(self, loca, direc):
        r, c = loca
        self.row = r
        self.col = c
        self.dire = direc
        self.sleep = False # is the bear asleep
        self.tSleep = 0 # how long has the bear been asleep 
        self.invalid = False
        
    def __str__(self):
        info = ''
        info += ("Row: " + str(self.row) + " Col: " + str(self.col) + '\n')
        info += ("Travel Dir: " + self.dire + '\n')
        info += ("Asleep? --> " + str(self.sleep))
        
        print("Berries: {}".format(self.eat))
        return info
     
    
    def move(self, tourists, field):
        ateR = 0
        justAte = 0
        while(1):
            if self.row < 0 or self.row > len(field) - 1:
                self.invalid = True
                break
            if self.col < 0 or self.col > len(field[0]) - 1:
                self.invalid = True
                break
            
            if self.sleep == True:
                if self.tSleep >= 2:
                    self.sleep = False
                    self.tSleep = 0
                    break
                else:
                    self.tSleep += 1
                    break
            else:
                for t in tourists:
                    if t.row == self.row and t.col == self.col:
                        self.sleep = True
                        self.tSleep = 0
                        t.goHome = True
                        
                toEat = field[self.row][self.col]
                
                if self.sleep == False:
                    if ateR == 30:
                        break
                    elif toEat <= (30 - ateR):
                        ateR += toEat
                        justAte = toEat
                        field[self.row][self.col] -= toEat
                        
                    else:
                        justAte = 30 - ateR
                        ateR = 30
                        field[self.row][self.col] -= justAte
                        break
                    if ateR != 30:
                        self.changeCoor()
    
    
            
        
    def changeCoor(self):
        move = self.dire
        if move == 'N':
            self.row = self.row - 1
        elif move == 'S':
            self.row = self.row + 1
        elif move == 'W':
            self.col = self.col - 1
        elif move == 'E':
            self.col = self.col + 1
        elif move == 'NW':
            self.row = self.row - 1
            self.col = self.col - 1
        elif move == 'SW':
            self.row = self.row + 1
            self.col = self.col - 1
        elif move == 'NE':
            self.row = self.row - 1
            self.col = self.col + 1
        elif move == 'SE':
            self.row = self.row + 1
            self.col = self.col + 1
    
    
'''
Function testing
l = (0,0)
d = 'SE'
b = Bear(l, d)
print(b)
print()
print('-------------') 
b.move(-1)
print(b)
print()
b.move(10)
print(b)
print()
b.move(10)
print(b)
print()
b.move(10)
print(b)
print()
b.move(10)
print(b)
print()
'''