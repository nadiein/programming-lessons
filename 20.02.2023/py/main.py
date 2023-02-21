# For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).

# E. g., with the input [3, 4, 2], your code should return 1 because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.

# Beware: powers grow incredibly fast. For example, 9 ^ (9 ^ 9) has more than 369 millions of digits. lastDigit has to deal with such numbers efficiently.

# Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list equals to 1.


class WrongType(Exception):
    pass

# Solution one
def solution(input_str, markers):
    # Split the input string into lines
    lines = input_str.split('\n')

    # Loop through each line
    for i in range(len(lines)):
        line = lines[i]

        # Find the first occurrence of any of the comment markers
        for marker in markers:
            index = line.find(marker)
            if index != -1:
                # Strip out the comment and any whitespace at the end of the line
                line = line[:index].rstrip()
                break

        # Update the line in the array
        lines[i] = line

    # Join the lines back into a single string and return it
    return '\n'.join(lines)


case = ['apples, pears # and bananas\ngrapes\nbananas !apples', ['#', '!']]

import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('solution(case[0], case[1])')

    start_time = time.time()
    solution(case[0], case[1])
    end_time = time.time()

    print('', end_time - start_time)
