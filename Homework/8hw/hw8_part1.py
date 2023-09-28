# -*- coding: utf-8 -*-
"""
Created on Fri Dec  9 18:18:20 2022

@author: szetok2
"""

import json
from BerryField import BerryField
from Bear import Bear
from Tourist import Tourist

if __name__ == "__main__":
    jsonN = input("Enter the json file name for the simulation => ").strip('\r')
    print(jsonN)
    print()
    
    '''
    jsonN = 'bears_and_berries_1.json'
    '''
    f = open(jsonN)
    
    data = json.loads(f.read())
    field = BerryField(data["berry_field"])
    aB = data['active_bears']
    rB = data['reserve_bears']
    aT = data['active_tourists']
    rT = data['reserve_tourists']
    
    activeB = []
    
    for a in aB:
        locat = (a[0], a[1])
        bear = Bear(locat, a[2])
        activeB.append(bear)
        
    activeT = []
    
    for t in aT:
        tour = Tourist(t[0], t[1])
        activeT.append(tour)
    
    print(field.printAll(activeB, activeT))
    print('Active Bears:')
    for bear in activeB:
        print('Bear at ({},{}) moving {}'.format(bear.row, bear.col, bear.dire))
        
    print()
    print('Active Tourists:')
    for tour in activeT:
        print('Tourist at ({},{}), {} turns without seeing a bear.'.format(tour.row, tour.col, tour.lastSeen))
        
    
    
