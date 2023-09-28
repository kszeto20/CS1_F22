# -*- coding: utf-8 -*-
"""
Created on Tue Dec  6 20:48:59 2022

@author: szetok2
"""


f_list = [ 19.4, 45.8, 25.2, -16, 82.19, 63.6, 45.1 ]
c_list = filter(lambda x: x>0, [((x-32) * (5/9)) for x in f_list])
line = ''
for word in c_list:
    line += '{:.2f}'.format(word)
    line += ' '
print(line.strip())
