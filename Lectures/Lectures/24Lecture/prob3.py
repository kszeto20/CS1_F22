# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 20:48:00 2022

@author: szetok2
"""


points = [ (4,2), (1,-3), (-4, -6), (4,9), (-7,8), (-5,2), (6,2) ]
s = sorted(points, key=lambda x: (x[0]**2 + x[1]**2)**(1/2), reverse=True)
print(s)
