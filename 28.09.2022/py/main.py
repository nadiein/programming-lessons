# implement a function that returns the number of possible patterns
# starting from a given first point, that have a given length.
# for a function countPatternsFrom(firstPoint, length), the parameter
# firstPoint is a single-character string corresponding to the point in
# the grid (i.e.: 'A') where your patterns start, and the parameter length
# is an integer indicating the number of points (length) every pattern must have.
# For example:
# countPatternsFrom("C", 2), should return the number of patterns starting
# from 'C' that have 2 two points. The return value in this case would be 5,
# because there are 5 possible patterns:
#(C -> B), (C -> D), (C -> E), (C -> F) and (C -> H).
# ---------------///////////////////////////---------------------
# Rules
### In a pattern, the dots/points cannot be repeated: they can only be used once, at most.
### In a pattern, any two subsequent dots/points can only be connected with direct straight lines in either of these ways:
### Horizontally: like (A -> B) in the example pattern image.
### Vertically: like (D -> G) in the example pattern image.
### Diagonally: like (I -> E), as well as (B -> I), in the example pattern image.
### Passing over a point between them that has already been 'used': like (G -> C) passing over E,
# in the example pattern image. This is the trickiest rule. Normally, you wouldn't be able to connect G to C,
# because E is between them, however when E has already been used as ### part the pattern you are tracing,
# you can connect G to C passing over E, because E is ignored, as it was already used once.

# A  B  C
# D  E  F
# G  H  I

import cProfile
from timeit import default_timer as t

def count_patterns_from(firstPoint, length) -> int:
    if length > 9:
        return 0
    grid = (('A', 'B', 'C'), ('D', 'E', 'F'), ('G', 'H', 'I'))
    res:int = 0
    return res

if __name__ == '__main__':
    cProfile.run('count_patterns_from("a", 2)')
    start = t()
    count_patterns_from('a', 10)
    end = t()
    print('profiler => ', end - start)
