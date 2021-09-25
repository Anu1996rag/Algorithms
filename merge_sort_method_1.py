"""Implementing merge sort"""


def merge_sort(array: list) -> list:
    if len(array) <= 1:
        return array

    mid = len(array) // 2

    left = merge_sort(array[:mid])
    right = merge_sort(array[mid:])

    return merge_two_sorted_list(left, right)


def merge_two_sorted_list(arr1, arr2):
    sorted_array = []
    i = j = 0

    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            sorted_array.append(arr1[i])
            i += 1
        else:
            sorted_array.append(arr2[j])
            j += 1

    while i < len(arr1):
        sorted_array.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_array.append(arr2[j])
        j += 1

    return sorted_array


if __name__ == "__main__":
    arr = [2, 5, 0, 1, 0]
    print(merge_sort(arr))
