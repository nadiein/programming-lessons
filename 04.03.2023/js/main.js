// Given an integer n (3 < n < 109), find the length of the smallest list of perfect squares which add up to n.

// Examples:
//    sum_of_squares(17) = 2
//    17 = 16 + 1 (16 and 1 are perfect squares).
//    sum_of_squares(15) = 4
//    15 = 9 + 4 + 1 + 1. There is no way to represent 15 as the sum of three perfect squares.
//    sum_of_squares(16) = 1
//    16 itself is a perfect square.

// Time constraints:
// easy test cases: n < 20
// harder test cases: 1000 < n < 15000
// hard test cases: 5e8 < n < 1e9
// hard test cases: 1e8 < n < 1e9


/* Solution one */
// The time complexity of this algorithm is O(n*sqrt(n))
export const sumOfSquaresOne = (n) => {
    // Create an array to store the minimum number of perfect squares needed
    // to add up to each number from 0 to n
    const dp = new Array(n + 1).fill(Infinity);
    dp[0] = 0;

    // Iterate over all numbers from 1 to n and find the minimum number
    // of perfect squares needed to add up to each number
    for (let i = 1; i <= n; i++) {
        for (let j = 1; j * j <= i; j++) {
            dp[i] = Math.min(dp[i], 1 + dp[i - j * j]);
        }
    }

    // Return the result for n
    return dp[n];
}

// Solution two
// The time complexity of this algorithm is O(n)
export const sumOfSquaresTwo = (n) => {
    // Find the largest perfect square less than or equal to n
    let largestSquare = Math.floor(Math.sqrt(n));

    // If n is already a perfect square, return 1
    if (largestSquare * largestSquare === n) {
        return 1;
    }

    // Check if n can be represented as the sum of two perfect squares
    for (let i = 1; i <= largestSquare; i++) {
        let j = Math.floor(Math.sqrt(n - i * i));

        if (i * i + j * j === n) {
            return 2;
        }
    }

    // Check if n can be represented as the sum of three perfect squares
    for (let i = 1; i <= largestSquare; i++) {
        for (let j = i; i * i + j * j <= n; j++) {
            let k = Math.floor(Math.sqrt(n - i * i - j * j));

            if (i * i + j * j + k * k === n) {
                return 3;
            }
        }
    }

    // If n cannot be represented as the sum of one, two, or three perfect squares,
    // it must require four perfect squares
    return 4;
}
