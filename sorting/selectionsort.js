let arr = [123, 42, 12, 9, 400, 23, 1, 0, 21];

function selectionSort(arr) {
    for (i = 0; i < arr.length; i++) {
        minVal = arr[i];
        minIndex = i;

        for (j = i+1; j < arr.length; j++) {
            if (arr[j] < minVal) {
                minVal = arr[j];
                minIndex = j
            }
        }

        let temp = arr[i];
        arr[i] = arr[minIndex];
        arr[minIndex] = temp;
    }

    return arr;
}

console.log(selectionSort(arr));
