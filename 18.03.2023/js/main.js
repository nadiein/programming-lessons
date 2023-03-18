// Refactor provided algorithms with awful running time of 2^n
// (as this function iterates through ALL 2^n-1 possibilities for a log of length n).
// function cutLog(p, n) {
//     if (n == 0) return 0;
//     let q = -1;
//     for (let i = 1; i <= n; i++) {
//         q = Math.max(q, p[i] + cutLog(p, n - i));
//     }
//     return q;
// }


/* Solution one */
// time complexity of the function is O(n^2)
export const cutLog = (p, n) => {
    let dp = new Array(n + 1).fill(0);

    for (let i = 1; i <= n; i++) {
        for (let j = 1; j <= i; j++) {
            dp[i] = Math.max(dp[i], p[j] + dp[i - j]);
        }
    }

    return dp[n];
}
