# For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).

# E. g., with the input [3, 4, 2], your code should return 1 because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.

# Beware: powers grow incredibly fast. For example, 9 ^ (9 ^ 9) has more than 369 millions of digits. lastDigit has to deal with such numbers efficiently.

# Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list equals to 1.


class WrongType(Exception):
    pass

# Solution one
# The algorithm first checks if the input list is empty, in which case it returns 1
# (this is the base case of the recursion). If the list is not empty, the function initializes
# the result to 1, and then iterates over the list in reverse order. For each element i in the list,
# it raises i to the power of the current result, modulo 10. If the current result is greater than or equal to 4,
# it takes the result modulo 4 and adds 4 to it, to handle the case where the exponent is a multiple of 4.
# Finally, the function returns the result modulo 10.
def last_digit(lst):
    if not lst:
        return 1
    result = 1
    for i in reversed(lst):
        result = i ** (result if result < 4 else result % 4 + 4)
    return result % 10


case = [937640, 767456, 981242]

import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('last_digit(case)')

    start_time = time.time()
    last_digit(case)
    end_time = time.time()

    print('', end_time - start_time)
