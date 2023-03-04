# Given an integer n (3 < n < 109), find the length of the smallest list of perfect squares which add up to n.

# Examples:
#    sum_of_squares(17) = 2
#    17 = 16 + 1 (16 and 1 are perfect squares).
#    sum_of_squares(15) = 4
#    15 = 9 + 4 + 1 + 1. There is no way to represent 15 as the sum of three perfect squares.
#    sum_of_squares(16) = 1
#    16 itself is a perfect square.

# Time constraints:
# easy test cases: n < 20
# harder test cases: 1000 < n < 15000
# hard test cases: 5e8 < n < 1e9
# hard test cases: 1e8 < n < 1e9


class WrongType(Exception):
    pass

# Solution one
# The time complexity of this algorithm is O(n*sqrt(n))
# because we are iterating through each number from 1 to n and for each number
# we are checking all possible perfect squares up to sqrt(n)
def sum_of_squares(n):
    # initialize list
    dp = [float('inf')] * (n+1)
    dp[0] = 0

    # iterate through each number
    for i in range(1, n+1):
        # check all possible perfect squares
        for j in range(1, int(i**0.5)+1):
            dp[i] = min(dp[i], dp[i-j*j] + 1)

    return dp[n] if dp[n] < float('inf') else -1



import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('sum_of_squares("15")')

    start_time = time.time()
    sum_of_squares(15)
    end_time = time.time()

    print('', end_time - start_time)
