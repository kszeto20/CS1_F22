# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 17:38:21 2022

@author: szetok2
"""
'''
Tourist Class
init = takes in a row and column
str = prints location, when the last bear was seen, if tourist is going home
check = checks if the tourist needs to go home
    --> if last seen >= 2, go home immediately
    --> else check if they see any bears at current turn
        --> if see a bear restart turn counter
        --> else, add to turn counter
        
sawBear = checks if the tourist can see a specified bear
'''

class Tourist(object):
    
    def __init__(self, r, c):
        self.row = r
        self.col = c
        self.lastSeen = 0
        self.goHome = False
        
    def __str__(self):
        info = ''
        
        info += ('Location --> Row: {} Col: {}\n'.format(self.row, self.col))
        info += ('Last seen: {}\n'.format(self.lastSeen))
        info += ('Going home: {}\n'.format(self.goHome))
        
        return info
    
    def check(self, bears):
        if(self.goHome != True):    
            if self.lastSeen >= 2:
                self.goHome = True
                
            totalSeen = 0
            for b in bears:
                if b.row == self.row and b.col == self.col:
                    self.goHome = True
                    
                    self.lastSeen = 0
                    break
                elif (self.sawBear(b.row, b.col)):
                    totalSeen += 1
            if(self.goHome == False):
                if totalSeen >= 3:
                    self.goHome = True
                elif totalSeen < 3 and totalSeen > 0:
                    self.goHome == False
                    self.lastSeen = 0
                else:
                    self.lastSeen += 1
        
    
    def sawBear(self, bR, bC):
        lastSeen = 0
        rows = bR - self.row
        cols = bC - self.col
        
        d = pow((pow(rows, 2) + pow(cols, 2)), 1/2)
        if d <= 4 and d > 0:
            return True
        else:
            return False
    
    
        

'''
testing
a = Tourist(10, 12)

b = a.sawBear(11, 15.5)
print(b)
print('----------------')

a.checkHome(2)
print(a)
a.checkHome(0)
print(a)
a.checkHome(0)
print(a)
a.checkHome(0)
print(a)
a.checkHome(2)
print(a)
'''