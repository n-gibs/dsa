let arr = [123, 42, 12, 9, 400, 23, 1, 0, 21];

function bubbleSort(arr) {
    for (i = 0; i < arr.length; i++) {
        for (j = arr.length - 1; j > i; j--) {

            if (arr[j-1] > arr[j]) {
                let temp = arr[j];
                arr[j] = arr[j-1]
                arr[j-1] = temp
            }
        }
    }
    return arr;
}

console.log(bubbleSort(arr));
