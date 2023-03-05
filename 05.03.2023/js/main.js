// function should make a list of strings representing all of the ways that can balance n pairs of parentheses

// Examples
//     balanced_parens(0) => [""]
//     balanced_parens(1) => ["()"]
//     balanced_parens(2) => ["()()","(())"]
//     balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]


/* Solution one */
// The time complexity of this algorithm is O(n*sqrt(n))
export const balancedParensOne = (n) => {
    if (n === 0) {
        return [''];
    } else {
        const result = [];

        for (let i = 0; i < n; i++) {
            const lefts = balancedParensOne(i);
            const rights = balancedParensOne(n - i - 1);

            for (let j = 0; j < lefts.length; j++) {
                for (let k = 0; k < rights.length; k++) {
                    result.push(`(${lefts[j]})${rights[k]}`);
                }
            }
        }

        return result;
    }
}

/* Solution one */
// time complexity of the improved algorithm is O(n^2 * C_n),
// where C_n is the nth Catalan number, which is the number of possible combinations
// of balanced parentheses with n pairs. This is much better than the original algorithm,
// since C_n is on the order of 4^n / n^(3/2). 
export const balancedParensTwo = (n) => {
    const dp = [['']];

    for (let i = 1; i <= n; i++) {
        const result = [];

        for (let j = 0; j < i; j++) {
            const lefts = dp[j];
            const rights = dp[i - j - 1];

            for (let k = 0; k < lefts.length; k++) {
                for (let l = 0; l < rights.length; l++) {
                    result.push(`(${lefts[k]})${rights[l]}`);
                }
            }
        }
        dp.push(result);
    }

    return dp[n];
}