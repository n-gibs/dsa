arr = [123, 42, 12, 9, 400, 23, 1, 0, 21]

def insertionSort(arr):
    for i in range(0, len(arr)):
            temp = arr[i]
            j = i -1
            while (arr[j] > temp and j >= 0):
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = temp

    return arr


print(insertionSort(arr))