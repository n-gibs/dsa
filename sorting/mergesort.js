function merge(leftArr, rightArr) {
    let resultArray = [],
        leftIndex = 0,
        rightIndex = 0;

    // We will concatenate values into the resultArray in order
    while (leftIndex < leftArr.length && rightIndex < rightArr.length) {
        if (leftArr[leftIndex] < rightArr[rightIndex]) {
            resultArray.push(leftArr[leftIndex]);
            leftIndex++; // move left array cursor
        } else {
            resultArray.push(rightArr[rightIndex]);
            rightIndex++; // move right array cursor
        }
    }

    // We need to concat here because there will be one element remaining
    // from either left OR the right
    return resultArray
        .concat(leftArr.slice(leftIndex))
        .concat(rightArr.slice(rightIndex));
}

function mergeSort(unsortedArray) {
    // No need to sort the array if the array only has one element or empty
    if (unsortedArray.length <= 1) {
        return unsortedArray;
    }
    // In order to divide the array in half, we need to figure out the middle
    const middle = Math.floor(unsortedArray.length / 2);

    // This is where we will be dividing the array into left and right
    const leftArr = unsortedArray.slice(0, middle);
    const rightArr = unsortedArray.slice(middle);

    // Using recursion to combine the left and right
    return merge(mergeSort(leftArr), mergeSort(rightArr));
}

let arr = [123, 42, 12, 9, 400, 23, 1, 0, 21];
console.log(mergeSort(arr));
