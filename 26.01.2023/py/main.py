# Given a mathematical expression as a string you must return the result as a number.
# Decompose n! (factorial n) into its prime factors
# Examples:
#       n = 12; decomp(12) -> '2^10 * 3^5 * 5^2 * 7 * 11'
#       since 12! is divisible by 2 ten times, by 3 five times, by 5 two times and by 7 and 11 only once.
#       n = 22; decomp(22) -> '2^19 * 3^9 * 5^4 * 7^3 * 11^2 * 13 * 17 * 19'
#       n = 25; decomp(25) -> 2^22 * 3^10 * 5^6 * 7^3 * 11^2 * 13 * 17 * 19 * 23


class WrongType(Exception):
    pass

# Solution one
def decomp(n):
    # Initialize an empty dictionary to store the prime factors
    primeFactors = {}

    # Iterate from 2 to n
    for i in range(2, n+1):
        currentNum = i

        # Iterate from 2 to the square root of the current number
        for j in range(2, int(currentNum**0.5)+1):
            # While the current number is divisible by j, add j to the primeFactors dictionary and divide the current number by j
            while currentNum % j == 0:
                if j in primeFactors:
                    primeFactors[j] += 1
                else:
                    primeFactors[j] = 1
                currentNum = currentNum // j

        # If the current number is greater than 1, it is a prime factor
        if currentNum > 1:
            if currentNum in primeFactors:
                primeFactors[currentNum] += 1
            else:
                primeFactors[currentNum] = 1

    # Sort the prime factors by key
    sortedPrimeFactors = sorted(primeFactors.keys())

    # Create a string of the prime factors in the form 'p1^e1 * p2^e2 * ... * pn^en'
    result = ''

    for i in range(len(sortedPrimeFactors)):
        if primeFactors[sortedPrimeFactors[i]] > 1:
            result += f"{sortedPrimeFactors[i]}^{primeFactors[sortedPrimeFactors[i]]}"
        else:
            result += f"{sortedPrimeFactors[i]}"

        if i < len(sortedPrimeFactors) - 1:
            result += ' * '

    return result


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('')

    start_time = time.time()
    end_time = time.time()
    print('first approach timestamp', end_time - start_time)
