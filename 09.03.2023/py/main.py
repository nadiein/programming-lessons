# Given two strings s1 and s2, we want to visualize how different the two strings are.
# We will only take into account the lowercase letters (a to z).
# First let us count the frequency of each lowercase letters in s1 and s2.


class WrongType(Exception):
    pass

# Solution one
# time complexity of the algorithm is O(n log n), where n is the length of the resulting string
def mix(s1, s2):
    freq1 = {c: s1.count(c) for c in set(s1) if c.islower() and s1.count(c) > 1}
    freq2 = {c: s2.count(c) for c in set(s2) if c.islower() and s2.count(c) > 1}
    res = []

    for c in set(freq1.keys()) | set(freq2.keys()):
        if c in freq1 and c in freq2:
            if freq1[c] > freq2[c]:
                res.append('1:' + c * freq1[c])
            elif freq2[c] > freq1[c]:
                res.append('2:' + c * freq2[c])
            else:
                res.append('=:' + c * freq1[c])
        elif c in freq1:
            res.append('1:' + c * freq1[c])
        else:
            res.append('2:' + c * freq2[c])

    return '/'.join(sorted(res, key=lambda x: (-len(x), x)))


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('mix("Are they here", "yes, they are here")')

    start_time = time.time()
    mix('Are they here", "yes, they are here')
    end_time = time.time()

    print('', end_time - start_time)
