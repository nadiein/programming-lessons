// John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper
// a list of distances between these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving
// and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

// Which distances, hence which towns, they will choose so that the sum of the distances is the biggest
// possible to please Mary and John?

// Example:
// With list ls and 3 towns to visit they can make a choice between:
// [50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60]

// The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

// The biggest possible sum taking a limit of 174 into account is then 173
// and the distances of the 3 corresponding towns is [55, 58, 60].

// The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters t
// (maximum sum of distances, integer >= 0), k (number of towns to visit, k >= 1)
// and ls (list of distances, all distances are positive or zero integers and this list has at least one element).
// The function returns the "best" sum ie the biggest possible sum of k distances less than or equal to
// the given limit t, if that sum exists, or otherwise nil, null, None, Nothing, depending on the language.

// Examples:
//     ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163

//     xs = [50] choose_best_sum(163, 3, xs) -> nil (or null or ... or -1 (C++, C, D, Rust, Swift, Go, ...)

//     ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228


/* Solution one */
// time complexity of the function is O(n^k), where n is the length of the list ls.
// This is because it generates all possible combinations of k towns from the list using a loop
// that runs n - k + 1 times. The function also performs a constant-time check for each combination,
// which doesn't affect the overall time complexity.
export const chooseBestSumOne = (t, k, ls) => {
    let maxSum = -1;

    function recursiveChooseBestSum(t, k, ls, start, currSum) {
        if (k === 0) {
            if (currSum > maxSum && currSum <= t) {
                maxSum = currSum;
            }
            return;
        }

        for (let i = start; i <= ls.length - k; i++) {
            recursiveChooseBestSum(t, k - 1, ls, i + 1, currSum + ls[i]);
        }
    }

    recursiveChooseBestSum(t, k, ls, 0, 0);

    return maxSum === -1 ? null : maxSum;
}

/* Solution one */
// time complexity of the function is O(n^k), where n is the length of the list ls.
// This is because it generates all possible combinations of k towns from the list using a loop
// that runs 2^n times, and each iteration of the loop performs a constant-time check for each combination.
// However, the stack-based approach has a lower memory overhead compared to the recursive approach,
// since it doesn't create new function calls for each combination.
export const chooseBestSumTwo = (t, k, ls) => {
    let maxSum = -1;
    let stack = [{ index: 0, sum: 0, count: 0 }];

    while (stack.length > 0) {
        const { index, sum, count } = stack.pop();

        if (count === k) {
            if (sum > maxSum && sum <= t) {
                maxSum = sum;
            }
        } else if (index < ls.length) {
            stack.push({ index: index + 1, sum, count });
            stack.push({ index: index + 1, sum: sum + ls[index], count: count + 1 });
        }
    }

    return maxSum === -1 ? null : maxSum;
}