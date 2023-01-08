# Write a function, which takes a non-negative integer (seconds)
# as input and returns the time in a human-readable format (HH:MM:SS)
# Constraints:
# HH = hours, padded to 2 digits, range: 00 - 99
# MM = minutes, padded to 2 digits, range: 00 - 59
# SS = seconds, padded to 2 digits, range: 00 - 59
# The maximum time never exceeds 359999 (99:59:59)


class WrongType(Exception):
    pass

# Solution one
def make_readable(seconds):
    hours = seconds // 3600
    minutes = (seconds % 3600) // 60
    seconds = seconds % 60

    return f"{hours:02d}:{minutes:02d}:{seconds:02d}"


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('make_readable(359999)')

    start_time = time.time()
    make_readable(359999)
    end_time = time.time()
    print('first approach timestamp', end_time - start_time)
