# -*- coding: utf-8 -*-
"""
Created on Sat Jan  4 20:19:29 2020

@author: Gurudas

Selection Sort Algorithm
"""

""" Actual Logic for the Selection Sort"""

def findSmallest(arr):
    smallest = arr[0] #considering first element as smallest element
    smallest_index = 0 #shows the index of the smallest element
    
    for i in range(len(arr)): #going through each element in the array
        if arr[i] < smallest : #if an element is smaller than the considered smallest element
            smallest = arr[i] #assign the new smaller element to the variable smallest
            smallest_index = i #assign the index position of the new smallest element to the variable
    return smallest_index     #returns the position of the smallest element 


"""Function for Selection sort """

def selectionSort(arr):
    new_arr = [] #new empty list / array
    for i in range(len(arr)):
        smallest = findSmallest(arr)  #calling the function and storing the value to variable
        new_arr.append(arr.pop(smallest)) #attaching the element at the position "smallest" to new array
    return new_arr  #returning the newly sorted array

"""Calling the function """

print(selectionSort([1,4,5,3,6,7]))
