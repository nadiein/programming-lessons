// Calculate fib(n) where:

// fib(0) := 0
// fib(1) := 1
// fin(n + 2) := fib(n + 1) + fib(n)
// Write an algorithm that can handle n up to 2000000.

// Your algorithm must output the exact integer answer, to full precision.
// Also, it must correctly handle negative numbers as input.

// HINT I: Can you rearrange the equation fib(n + 2) = fib(n + 1) + fib(n) to
// find fib(n) if you already know fib(n + 1) and fib(n + 2)? Use this to reason
// what value fib has to have for negative values.


/* Solution one */
export const fib = (n) => {
    if (n === 0) {
        return 0n;
    } else if (n === 1) {
        return 1n;
    }

    // Initialize Fibonacci numbers
    let fibMinus1 = 1n;
    let fibMinus2 = 0n;
    let fib = 0n;

    // Calculate Fibonacci numbers using dynamic programming
    for (let i = 2; i <= Math.abs(n); i++) {
        fib = fibMinus1 + fibMinus2;
        fibMinus2 = fibMinus1;
        fibMinus1 = fib;
    }

    // Handle negative inputs
    if (n < 0 && n % 2 === 0) {
        fib = -fib;
    }

    return fib;
}