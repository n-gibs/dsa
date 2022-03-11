def binary_search(arr, left, right, target):

    if left < right :

        mid = left + (right - left) // 2

        if arr[mid] == target:

            return mid

        elif arr[mid] > target:
            return binary_search(arr, left, mid -1, target)

        else:
            return binary_search(arr, mid + 1, right, target)

    else:
        return -1


arr = [2, 3, 4, 10, 40]
x = 10
result = binary_search(arr, 0, len(arr) -1, x)
assert result == 3

arr = [2, 3, 4, 10, 40]
x = 11
result = binary_search(arr, 0, len(arr) -1, x)
assert result == -1

arr = [2, 3, 4, 10, 40]
x = 2
result = binary_search(arr, 0, len(arr) -1, x)
assert result == 0
