import random

def helper(arr, start, end):

    #leaf worker
    if start >= end:
        return

    smaller = start +1
    bigger = end

    while smaller <= bigger:
        if arr[smaller] <= arr[start]:
            smaller+=1
        elif arr[bigger] > arr[start]:
            bigger -=1
        else:
            arr[smaller], arr[bigger] = arr[bigger], arr[smaller]
            smaller+=1
            bigger -=1

    arr[start], arr[bigger] = arr[bigger], arr[start]

    helper(arr, start, smaller - 1)
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