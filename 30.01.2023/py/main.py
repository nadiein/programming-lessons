# In this kata, your task is to create all permutations of a non-empty input string and remove duplicates, if present.
# Create as many "shufflings" as you can!


class WrongType(Exception):
    pass

# Solution one
def permutations_1(string):
    if len(string) <= 1:
        return [string]

    result = []

    for i, c in enumerate(string):
        for p in permutations_1(string[:i] + string[i+1:]):
            result.append(c + p)

    return sorted(list(set(result)))

# Solution two
import itertools

def permutations_2(string):
    return sorted(list(set([''.join(p) for p in itertools.permutations(string)])))


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('')

    start_time = time.time()
    end_time = time.time()
    print('', end_time - start_time)
