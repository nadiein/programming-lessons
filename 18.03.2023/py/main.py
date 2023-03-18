# Refactor provided algorithms with awful running time of 2^n
# (as this function iterates through ALL 2^n-1 possibilities for a log of length n).
# def cut_log(p, n):
#     if (n == 0):
#         return 0
#     q = -1
#     for i in range(1, n+1):
#         q = max(q, p[i] + cut_log(p, n-i))
#     return q


class WrongType(Exception):
    pass

# Solution one
# time complexity is O(n^2)
def cut_log(p, n):
    memo = [0] * (n+1)  # initialize memoization array

    for i in range(1, n+1):
        max_val = float('-inf')

        for j in range(1, i+1):
            if j == i:
                max_val = max(max_val, p[j])
            else:
                max_val = max(max_val, memo[j] + memo[i-j])

        memo[i] = max_val

    return memo[n]


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('cut_log(230, 4, xs)')

    start_time = time.time()
    cut_log(230, 4, xs)
    end_time = time.time()

    print('', end_time - start_time)
