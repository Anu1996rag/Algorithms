def bubble_sort(arr, key=None):
    n = len(arr)

    for i in range(0, n - 1):
        swapped = False
        for j in range(0, n - i - 1):
            a = arr[j][key]
            b = arr[j+1][key]
            if a > b:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


elements = [
    {'name': 'mona', 'transaction_amount': 1000, 'device': 'iphone-10'},
    {'name': 'dhaval', 'transaction_amount': 400, 'device': 'google pixel'},
    {'name': 'kathy', 'transaction_amount': 200, 'device': 'vivo'},
    {'name': 'aamir', 'transaction_amount': 800, 'device': 'iphone-8'},
]

bubble_sort(elements, key='transaction_amount')
print(elements)
