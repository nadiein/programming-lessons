# John and Mary want to travel between a few towns A, B, C ... Mary has on a sheet of paper
# a list of distances between these towns. ls = [50, 55, 57, 58, 60]. John is tired of driving
# and he says to Mary that he doesn't want to drive more than t = 174 miles and he will visit only 3 towns.

# Which distances, hence which towns, they will choose so that the sum of the distances is the biggest
# possible to please Mary and John?

# Example:
# With list ls and 3 towns to visit they can make a choice between:
# [50,55,57],[50,55,58],[50,55,60],[50,57,58],[50,57,60],[50,58,60],[55,57,58],[55,57,60],[55,58,60],[57,58,60]

# The sums of distances are then: 162, 163, 165, 165, 167, 168, 170, 172, 173, 175.

# The biggest possible sum taking a limit of 174 into account is then 173
# and the distances of the 3 corresponding towns is [55, 58, 60].

# The function chooseBestSum (or choose_best_sum or ... depending on the language) will take as parameters t
# (maximum sum of distances, integer >= 0), k (number of towns to visit, k >= 1)
# and ls (list of distances, all distances are positive or zero integers and this list has at least one element).
# The function returns the "best" sum ie the biggest possible sum of k distances less than or equal to
# the given limit t, if that sum exists, or otherwise nil, null, None, Nothing, depending on the language.

# Examples:
#     ts = [50, 55, 56, 57, 58] choose_best_sum(163, 3, ts) -> 163

#     xs = [50] choose_best_sum(163, 3, xs) -> nil (or null or ... or -1 (C++, C, D, Rust, Swift, Go, ...)

#     ys = [91, 74, 73, 85, 73, 81, 87] choose_best_sum(230, 3, ys) -> 228


class WrongType(Exception):
    pass

# Solution one
# time complexity of O(n^k), where n is the length of the distance list ls
import itertools

def choose_best_sum_one(t, k, ls):
    best_sum = None
    
    # Generate all combinations of k towns from the list of distances
    for towns in itertools.combinations(ls, k):
        total_distance = sum(towns)
        
        # If the total distance is less than or equal to the limit and
        # it's greater than the current best sum, update the best sum
        if total_distance <= t and (best_sum is None or total_distance > best_sum):
            best_sum = total_distance
            
    # If no valid sum was found, return None
    if best_sum is None:
        return None
    
    return best_sum

# Solution two
# time complexity of this implementation is O(n choose k), where n is the length of the list ls,
# and k is the number of towns to visit
def choose_best_sum_two(t, k, ls):
    if len(ls) < k:
        return None

    if k == 1:
        return max((d for d in ls if d <= t), default=None)

    max_sum = None

    for i, d in enumerate(ls):
        sum_rest = choose_best_sum_two(t - d, k - 1, ls[i+1:])

        if isinstance(sum_rest, int):
            sum_rest = [sum_rest]
        if sum_rest is not None:

            for s in sum_rest:
                if max_sum is None or d + s > max_sum:
                    max_sum = d + s

    return max_sum


import cProfile
import time
from timeit import default_timer as timer


xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]


if __name__ == '__main__':
    cProfile.run('choose_best_sum_one(230, 4, xs)')
    cProfile.run('choose_best_sum_two(230, 4, xs)')

    start_time = time.time()
    choose_best_sum_one(230, 4, xs)
    choose_best_sum_two(230, 4, xs)
    end_time = time.time()

    print('', end_time - start_time)
