arr = [123, 42, 12, 9, 400, 23, 1, 0, 21]

def selectionSort(arr):
    for i in range(0, len(arr)):
        minVal = arr[i]
        minIndex = i

        for j in range(i+1, len(arr)):

            if (arr[j] < minVal):
                minVal = arr[j]
                minIndex = j

        arr[i], arr[minIndex] = arr[minIndex], arr[i]

    return arr

print(selectionSort(arr))