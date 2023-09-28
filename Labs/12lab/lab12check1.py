# -*- coding: utf-8 -*-
"""
Created on Wed Dec  7 02:36:04 2022

@author: szetok2
"""

'''


To make sure you understand this, show the sequence of calls made by
print(add(5,3))
You may add print statements to show the results.
Building on this idea, now write a recursive function to multiply two non-negative integers
using only the add function we’ve just defined, together with +1, -1 and the equality with 0
test. Call this function mult. Demonstrate the result by multiplying 8 and 3. As a recursive
function mult(8,3), mult can call itself of course.

'''
def add(m,n):
    if n == 0:
        return m
    else:
        return add(m,n-1) + 1
    
def mult(m, n):
    if n == 0 or m == 0:
        return 0
    else:
        return add(m, mult(m, n - 1))

def power(x, n):
    if n == 0:
        return 1
    else:
        return mult(x, power(x, n - 1))    
    
print(add(5,3))
print(mult(5, 3))
print(power(5, 3))