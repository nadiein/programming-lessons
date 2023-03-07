// Write an algorithm that takes an array and moves all of the zeros to the end,
// preserving the order of the other elements.


/* Solution one */
// time complexity of the algorithm is O(n), where n is the length of the input array.
// This is because we need to iterate over the input array once to separate the zeros from the non-zeros,
// and then concatenate the two arrays, which takes O(n) time.
export const moveZerosOne = (arr) => {
    let zeros = [];
    let nonZeros = [];

    // Separate zeros from non-zeros
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] === 0) {
            zeros.push(arr[i]);
        } else {
            nonZeros.push(arr[i]);
        }
    }

    // Concatenate non-zeros and zeros
    return nonZeros.concat(zeros);
}

/* Solution one */
// time complexity of the algorithm is O(n)
// improved the performance of this algorithm by doing the separation and concatenation in a single loop
export const moveZerosTwo = (arr) => {
    let j = 0; // index of first zero

    // Iterate through the array, swapping non-zeros with zeros
    for (let i = 0; i < arr.length; i++) {
        if (arr[i] !== 0) {
            // Swap non-zero with first zero
            let temp = arr[j];

            arr[j] = arr[i];
            arr[i] = temp;
            j++;
        }
    }

    return arr;
}
