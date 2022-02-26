import random

def helper(arr, start, end):

    if start >= end:
        return
    # Do Lomuto's partitioning
    rand_int = random.randint(start, end)
    pivot_val = arr[rand_int]


    arr[start], arr[rand_int] = arr[rand_int], arr[start]
    smaller = start


    for bigger in range(start+1, end+1):
        if arr[bigger] < pivot_val:
            smaller += 1
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]

    arr[smaller], arr[start] = arr[start], arr[smaller]


    helper(arr, start, smaller)
    helper(arr, smaller + 1, end)


def quicksort(arr):
    helper(arr, 0, len(arr)-1)

    return arr

### TESTS ###
a = [14, 2, 8, 3, 5, 45, 6, 12]
result = quicksort(a)
print(result)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2, 8, 3, 5, 6, 45, 12]
result = quicksort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 45, 6, 2, 8, 3, 5, 12]
result = quicksort(a)
assert result == [2, 3, 5, 6, 8, 12, 14, 45]

a = [14, 2]
result = quicksort(a)
assert result == [2, 14]

a = [2]
result = quicksort(a)
assert result == [2]

a = []
result = quicksort(a)
assert result == []