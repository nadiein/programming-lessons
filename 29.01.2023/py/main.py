# Create a RomanNumerals class that can convert a roman numeral to and from an integer value.
# Modern Roman numerals are written by expressing each digit separately starting with the left
# most digit and skipping any digit with a value of zero.
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
# 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.


class WrongType(Exception):
    pass

# Solution one


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('')

    start_time = time.time()
    end_time = time.time()
    print('', end_time - start_time)
