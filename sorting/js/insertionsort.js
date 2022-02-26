let arr = [123, 42, 12, 9, 400, 23, 1, 0, 21];

function insertionSort(arr) {
for (i = 0; i < arr.length; i++) {
        let temp = arr[i];
        let j = i -1;
        while (arr[j] > temp && j >= 0) {
            arr[j+1] = arr[j];
            j--;
        }
        arr[j+1] = temp
    }
    return arr;
}

console.log(insertionSort(arr));
