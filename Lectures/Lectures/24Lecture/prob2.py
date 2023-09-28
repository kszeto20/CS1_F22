# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 20:46:16 2022

@author: szetok2
"""


points = [ (4,2), (1,-3), (-4, -6), (6,9), (3,8), (-5,2), (6,2) ]

minx = filter(lambda x: x[0]>0 and x[1]>0, points)

mins = min(list(minx))[0]
print(mins)
