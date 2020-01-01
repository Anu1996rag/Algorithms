def binary_search (sorted_list , item):
    low = 0
    high = len(sorted_list) - 1 #low and high keeps the track of which part you want to search in 
    
    while low <= high : #while you haven't came down searching upto one element
        mid = (low + high) // 2 #calculating the middle element
        guess = sorted_list[mid]
        
        if guess == item : #if the item found in the first search 
            pos = mid
            return pos + 1
        elif guess > item : #if the guess element is less than the item we are searching for
            high = mid - 1   #make the middle + 1 element as low and discard the remaining element
        else:
            low = mid + 1 #if the guess element is greater than the search element then 
                            #make the middle - 1 element as high and discard the remaining element
    return None #if the item or the search element does not exist , retuen None

n = int(input("Enter no. of elements:"))

my_list = [] #empty list

for i in range(n):    #taking the no. of elements in the given range 
    my_list.append(int(input()))
    
key = int(input("Enter element you want to search :")) #element we want to search for 

my_list = sorted(my_list)  #sorting the list before passing it to the function 

position = binary_search(my_list,key) #calling the function and returning the value 

if position == None : #that means the function has did not found any element
    print("No element found")
else :
    print("Element found at position:",position)
 
