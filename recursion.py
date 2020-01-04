# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 20:38:11 2020

@author: Gurudas

Recursion Basics
"""

#print 10 numbers using recursion

def countdown(i):
    print(i)
    if i <= 0:
        return 
    else:
        countdown(i-1)

print(countdown(10))

#factorial no.

def factorial(n):
    if n == 1:
        return 1
    else:
        return n*factorial(n-1)
    
print(factorial(6))

