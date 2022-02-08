function merge(leftArr, rightArr) {
	let results = [];

	let i = 0;
	let j = 0;

	// compare smallest value between two arrays, move pointer on the array that has the smaller value. Otherwise, move pointer in the array
	// that has the larger value...
	while (i < leftArr.length && j < rightArr.length) {
		if (leftArr[i] < rightArr[j]) {
			results.push(leftArr[i]);
			i++;
		} else {
			results.push(rightArr[j]);
			j++;
		}
	}

	// push in remaining values from either array that has values left
	while (i < leftArr.length) {
		results.push(leftArr[i]);
		i++;
	}
	while (j < rightArr.length) {
		results.push(rightArr[j]);
		j++
	}

	return results;
}

function merge_sort(arr) {
    // No need to sort the array if the array only has one element or empty
    if (arr.length <= 1) {
        return arr;
	}

	const mid = Math.floor(arr.length / 2);
	// equal left half
	const left = merge_sort(arr.slice(0, mid));
	// equal right half
	const right = merge_sort(arr.slice(mid));

	return merge(left, right);
}

let arr = [123, 42, 12, 9, 400, 23, 1, 0, 21];
console.log(merge_sort(arr));
