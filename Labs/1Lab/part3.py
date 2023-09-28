# -*- coding: utf-8 -*-
"""
Created on Wed Sep 14 10:28:03 2022

@author: szetok2
"""

base10size = input("Disk size in GB => ")
print(base10size)

base10size = int(base10size)

base2size = int((((base10size) * (10 ** 9)) / (2 ** 30)))

lost_size = int(base10size - base2size)

print("{0} GB in base 10 is actually {1} GB in base 2, {2} GB less than advertised.".format(base10size, base2size, lost_size))

print("Input: ", '*' * base10size)
print("Actual:", '*' * base2size)
