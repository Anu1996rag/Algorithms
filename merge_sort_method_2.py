"""Implementing merge sort"""


def merge_sort(array: list) -> None:
    if len(array) <= 1:
        return

    mid = len(array) // 2

    left = array[:mid]
    right = array[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_list(left, right, array)


def merge_two_sorted_list(arr1, arr2, arr3):
    i = j = k = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            arr3[k] = arr1[i]
            i += 1
        else:
            arr3[k] = arr2[j]
            j += 1
        k += 1

    while i < len(arr1):
        arr3[k] = arr1[i]
        i += 1
        k += 1
    while j < len(arr2):
        arr3[k] = arr2[j]
        j += 1
        k += 1


if __name__ == '__main__':
    test_cases = [
        [10, 3, 15, 7, 8, 23, 98, 29],
        [],
        [3],
        [9, 8, 7, 2],
        [1, 2, 3, 4, 5]
    ]

    test_results = [
        [3, 7, 8, 10, 15, 23, 29, 98],
        [],
        [3],
        [2, 7, 8, 9],
        [1, 2, 3, 4, 5]
    ]

    for i, j in zip(test_cases, test_results):
        merge_sort(array=i)
        assert i == j

