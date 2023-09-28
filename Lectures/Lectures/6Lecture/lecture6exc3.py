# -*- coding: utf-8 -*-
"""
Created on Fri Sep 16 17:53:34 2022

@author: szetok2
"""

n1 = input("Enter the first number: ")
print(n1)

n2 = input("Enter the second number: ")
print(n2)


num1 = float(n1)
num2 = float(n2)

if(num1 > 10 and num2 > 10):
    print("Both are above 10.")
elif(num1 < 10 and num2 < 10):
    print("Both are below 10.")
    
print("Average is {:.2f}".format((num1 + num2) / 2))