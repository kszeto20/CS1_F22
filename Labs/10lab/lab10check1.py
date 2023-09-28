# -*- coding: utf-8 -*-
"""
Created on Wed Nov 16 02:50:25 2022

@author: szetok2
"""

""" 
    This is the skeleton to demonstrate how to put Lab 10 together. 
    It provides an example to show the use of doctest. Note the function,
    addone(x) presented below has an additional 4 lines after 
    the normal function description. The lines beginning with '>>>'
    indicate examples of how the function can be called, and 
    the lines immediately after represent the expected return
    from the call. So, for example, 'addone(1)' should return '2'
    and 'addone(0) should return 1. These lines provide examples
    for a potential user of the lab10 module, but more importantly
    for this lab, they work with the doctest module to allow us to
    do automated testing. 
    
    Look at the file 'test_driver.py' for an example of how to use
    this testing information. Then come back here and change 
    the answer for one or both of the addone examples to 
    an incorrect value and run the testing again to see how a failing
    test is reported.
"""
import time
import random

def closest1(listN):
    '''
    should return closest pair
    
    >>> closest1([4.4, 5.3, 12, 14])
    (4.4, 5.3)
    >>> closest1([236, 3, 2000, 84, 234])
    (236, 234)
    >>> closest1([4.4, 334.8, 34, 334.2])
    (334.8, 334.2)
    
    '''
    if len(listN) < 2:
        return (None, None)
    
    first = listN[0]
    second = listN[1]
    diff = abs(listN[0] - listN[1])
    for i in range(len(listN)):
        for j in range(i + 1, len(listN)):
            aDiff = abs(listN[i] - listN[j])
            if aDiff < diff:
                first = listN[i]
                second = listN[j]
                diff = aDiff
                
    return (first, second)

def closest2(listN):
    '''
    should return closest pairs
    
    >>> closest2([12, 13, 3030, 43.44, 13.1])
    (13, 13.1)
    
    >>> closest2([234, 66, 55, 29, 23499, 10, 28.5, 42])
    (28.5, 29)
    
    >>> closest2([4])
    (None, None)
    '''
    if len(listN) < 2:
        return (None, None)
    
    cList = listN.copy()
    cList.sort() # nlogn
    
    beg = cList[0]
    end = cList[1]
    diff = abs(cList[0] - cList[1])
    for i in range(len(cList) - 1):
        if abs(cList[i] - cList[i+1]) < diff:
            beg = cList[i]
            end = cList[i + 1]
            diff = abs(beg - end)
            
    return (beg, end)

if __name__ == "__main__":
    a = []
    for i in range(10000):
        a.append(random.uniform(0.0, 1000.0))
    s1 = time.time()
    (i0,i1) = closest1(a)
    t1 = time.time() - s1
    print("Ver 1:  indices ({},{}); time {:.3f} seconds".format(i0,i1,t1))
    
    s2 = time.time()
    (i1,i2) = closest2(a)
    t2 = time.time() - s2
    print("Ver 2:  indices ({},{}); time {:.3f} seconds".format(i1,i2,t2))
