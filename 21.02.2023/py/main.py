# Calculate fib(n) where:

# fib(0) := 0
# fib(1) := 1
# fin(n + 2) := fib(n + 1) + fib(n)
# Write an algorithm that can handle n up to 2000000.

# Your algorithm must output the exact integer answer, to full precision.
# Also, it must correctly handle negative numbers as input.

# HINT I: Can you rearrange the equation fib(n + 2) = fib(n + 1) + fib(n) to
# find fib(n) if you already know fib(n + 1) and fib(n + 2)? Use this to reason
# what value fib has to have for negative values.


class WrongType(Exception):
    pass

# Solution one
def fib(n):
    # Handle negative input
    if n < 0:
        # Use the recurrence relation fib(n) = (-1)^(n+1) * fib(|n|) for negative n
        return (-1)**(n+1) * fib(abs(n))

    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 1

    # Dynamic programming: calculate Fibonacci numbers iteratively
    fib_n_minus_2 = 0
    fib_n_minus_1 = 1

    for i in range(2, n + 1):
        fib_n = fib_n_minus_1 + fib_n_minus_2
        fib_n_minus_2 = fib_n_minus_1
        fib_n_minus_1 = fib_n

    return fib_n


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('fib(1000)')

    start_time = time.time()
    fib(1000)
    print(fib(1000))
    end_time = time.time()

    print('', end_time - start_time)
