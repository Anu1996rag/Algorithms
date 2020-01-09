# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 20:38:11 2020

@author: Gurudas

Recursion Basics
"""

#print 10 numbers using recursion

def countdown(i):
    print(i)
    if i <= 0:   #base case
        return 
    else:
        countdown(i-1)  #recursion case

print(countdown(10))

#factorial no.

def factorial(n):
    if n == 1:  #base case
        return 1
    else:
        return n*factorial(n-1) #recursion case
    
print(factorial(6))

#calculating sum 

def summation(arr):
    if arr == []:
        return 0
    return arr[0] + summation(arr[1:])

print(summation([1,2,3]))
    
#to count the number of items in the list 

def count(lists):
    if lists == []:
        return 0
    return 1 + count(lists[1:])

print(count([1,2,3,4,5]))

#to find out the maximum number in the list

def maximum(arr):
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = maximum(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max

print(maximum([2,5,4,1]))
