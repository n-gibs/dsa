arr = [123, 42, 12, 9, 400, 23, 1, 0, 21];

def bubbleSort(arr):
    for i in range(0, len(arr)):
        for j in range(len(arr) -1, i):

            if arr[j-1] > arr[j]:
                arr[j-1], arr[j] = arr[j], arr[j-1]

    return arr

print(bubbleSort(arr))