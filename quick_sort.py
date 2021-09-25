# -*- coding: utf-8 -*-
"""
Created on Thu Jan  9 10:08:31 2020

@author: Gurudas

Quick Sort Algorithm
"""


def quicksort(arr):
    if len(arr) < 2:
        return arr  # base case ; arrays with 0 or 1 elements are already sorted
    else:
        pivot = arr[0]  # recursive case

        less = [i for i in arr[1:] if i <= pivot]  # sub- array of all the elements less than the pivot element

        greater = [i for i in arr[1:] if i > pivot]  # sub-array of all the elements greater than pivot element

        return quicksort(less) + [pivot] + quicksort(greater)  # clubbing the arrays together after sorting


print(quicksort([10, 5, 2, 3]))
