# -*- coding: utf-8 -*-
"""
Created on Wed Jan  1 11:51:12 2020

@author: Gurudas

Binary Search Algorithm
"""

def binary_search (sorted_list , item):
    low = 0
    high = len(sorted_list) - 1 #low and high keeps the track of which part you want to search in 
    
    while low <= high : #while you haven't came down searching upto one element
        mid = (low + high) // 2 #calculating the middle element
        guess = sorted_list[mid]
        
        if guess == item : #if the item found in the first search 
            return mid
        elif guess > item : #if the guess element is less than the item we are searching for
            high = mid - 1   #make the middle + 1 element as low and discard the remaining element
        else:
            low = mid + 1 #if the guess element is greater than the search element then 
                            #make the middle - 1 element as high and discard the remaining element
    return None #if the item or the search element does not exist , retuen None

my_list = [1,2,3,4,5,6,7,8,9]

print(binary_search(my_list, 3)) #calling the function and returning the value 
 

            
        

