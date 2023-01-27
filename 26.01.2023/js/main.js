// Decompose n! (factorial n) into its prime factors
// Examples:
//       n = 12; decomp(12) -> '2^10 * 3^5 * 5^2 * 7 * 11'
//       since 12! is divisible by 2 ten times, by 3 five times, by 5 two times and by 7 and 11 only once.
//       n = 22; decomp(22) -> '2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19'
//       n = 25; decomp(25) -> 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23

/* Solution one */
export const decomp1 = (n) => {
    // Initialize an empty object to store the prime factors
    let primeFactors = {};

    // Iterate from 2 to n
    for (let i = 2; i <= n; i++) {
        let currentNum = i;

        // Iterate from 2 to the square root of the current number
        for (let j = 2; j <= Math.sqrt(currentNum); j++) {
            // While the current number is divisible by j, add j to the primeFactors object and divide the current number by j
            while (currentNum % j === 0) {
                primeFactors[j] = (primeFactors[j] || 0) + 1;
                currentNum /= j;
            }
        }

        // If the current number is greater than 1, it is a prime factor
        if (currentNum > 1) {
            primeFactors[currentNum] = (primeFactors[currentNum] || 0) + 1;
        }
    }

    // Sort the prime factors by key
    let sortedPrimeFactors = Object.keys(primeFactors).sort((a, b) => a - b);

    // Create a string of the prime factors in the form 'p1^e1 * p2^e2 * ... * pn^en'
    let result = '';

    for (let i = 0; i < sortedPrimeFactors.length; i++) {
        if (primeFactors[sortedPrimeFactors[i]] > 1) {
            result += `${sortedPrimeFactors[i]}^${primeFactors[sortedPrimeFactors[i]]}`;
        } else {
            result += `${sortedPrimeFactors[i]}`
        }

        if (i < sortedPrimeFactors.length - 1) {
            result += ' * ';
        }
    }

    return result;
}

// Solution two: Best performance with complexity O(n log log n)
export const decomp2 = (n) => {
    let primeFactors = {};
    let primes = sieveOfEratosthenes(n);

    for (let i = 0; i < primes.length; i++) {
        let prime = primes[i];
        let exponent = 0;

        for (let j = prime; j <= n; j *= prime) {
            exponent += Math.floor(n / j);
        }

        primeFactors[prime] = exponent;
    }

    let result = '';

    for (let key in primeFactors) {

        if (primeFactors[key] > 1) {
            result += `${key}^${primeFactors[key]}`;
        } else {
            result += `${key}`;
        }

        if (key !== Object.keys(primeFactors)[Object.keys(primeFactors).length - 1]) {
            result += ' * ';
        }
    }

    return result;
}

const sieveOfEratosthenes = (n) => {
    let primes = new Array(n + 1);

    primes.fill(true);
    primes[0] = primes[1] = false;

    for (let i = 2; i <= Math.sqrt(n); i++) {

        if (primes[i]) {

            for (let j = i * i; j <= n; j += i) {
                primes[j] = false;
            }
        }
    }

    let result = [];

    for (let i = 2; i <= n; i++) {

        if (primes[i]) {
            result.push(i);
        }
    }

    return result;
}
