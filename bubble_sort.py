def bubble_sort(arr):
    n = len(arr)

    for i in range(0, n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


a = [31, 32, 34, 35]
print(bubble_sort(a))
