# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 18:55:35 2022

@author: szetok2
"""

'''
Program Outline:
    
make import statements
make all bear and tourist objects
Start configuration
for each iteration: (total of 5)
    grow
    spread 
    check bears
    cheack tourist
    print board and status of active and leaving bears and tourists
'''


# import statements
import json
from BerryField import BerryField
from Bear import Bear
from Tourist import Tourist
if __name__ == "__main__":
    jsonN = input("Enter the json file name for the simulation => ").strip('\r')
    print(jsonN)
    print()
    
    f = open(jsonN)
    
    data = json.loads(f.read())
    field = BerryField(data["berry_field"])
    aB = data['active_bears']
    rB = data['reserve_bears']
    aT = data['active_tourists']
    rT = data['reserve_tourists']
    
    # create all bear objects
    activeB = []
    
    for a in aB:
        locat = (a[0], a[1])
        bear = Bear(locat, a[2])
        activeB.append(bear)
        
    activeT = []
    
    for t in aT:
        tour = Tourist(t[0], t[1])
        activeT.append(tour)
        
    print('Starting Configuration')
    print(field.printAll(activeB, activeT))
    print('Active Bears:')
    for bear in activeB:
        print('Bear at ({},{}) moving {}'.format(bear.row, bear.col, bear.dire))
        
    print()
    print('Active Tourists:')
    for tour in activeT:
        print('Tourist at ({},{}), {} turns without seeing a bear.'.format(tour.row, tour.col, tour.lastSeen))
        
    
    i = 1
    while(i < 6):
        print()
        print('Turn: {}'.format(i))
        
        field.grow()
        field.spread()
        
        for bear in activeB:
            bear.move(activeT, field.field)
        
        for tour in activeT:
            tour.check(activeB)
            
        for be in activeB:
            if be.invalid == True:
                print('Bear at ({},{}) moving {} - Left the Field'.format(be.row, be.col, be.dire))
        
        updatedBears = []
        for bear in activeB:
            if bear.invalid == True:
                continue
            else:
                updatedBears.append(bear)
                
        activeB = updatedBears
        
        for to in activeT:
            if to.goHome == True:
                print('Tourist at ({},{}), {} turns without seeing a bear. - Left the Field'.format(to.row, to.col, to.lastSeen))
        
        updatedTour = []
        for tour in activeT:
            if tour.goHome == True:
                continue
            else:
                updatedTour.append(tour)
                
        activeT = updatedTour
        
        
        
        print(field.printAll(activeB, activeT))
        print('Active Bears:')
        for bear in activeB:
            if bear.sleep == True:
                print('Bear at ({},{}) moving {} - Asleep for {} more turns'.format(bear.row, bear.col, bear.dire, 3 - bear.tSleep))
            else:
                print('Bear at ({},{}) moving {}'.format(bear.row, bear.col, bear.dire))
        print()
        print('Active Tourists:')
        for tour in activeT:
            print('Tourist at ({},{}), {} turns without seeing a bear.'.format(tour.row, tour.col, tour.lastSeen))
        print()
        i += 1