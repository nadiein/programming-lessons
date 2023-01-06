# Complete the function to find the count of the most frequent item of an array.
# You can assume that input is an array of integers. For an empty array return 0


class WrongType(Exception):
    pass

# First solution: easiest way to find the count of the most frequent item of an array.
def most_frequent_item_count_1(collection):
    if not collection:
        return 0
    
    if not isinstance(collection, list):
        raise WrongType

    counts = {}
    max_item = collection[0]
    max_count = 1

    for item in collection:
        counts[item] = counts.get(item, 0) + 1
        if counts[item] > max_count:
            max_item = item
            max_count = counts[item]

    return max_count

# Second solution: shortest and fastest way to find the count of the most frequent item of an array.
from collections import Counter

def most_frequent_item_count_2(collection):
    if not isinstance(collection, list):
        raise WrongType

    return Counter(collection).most_common(1)[0][1] if collection else 0

# Third solution: shortest solution without counter lib
def most_frequent_item_count_3(collection):
    if not isinstance(collection, list):
        raise WrongType

    return collection.count(max(collection, key=collection.count)) if collection else 0


import cProfile
import time
from timeit import default_timer as timer

collection = [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3]

if __name__ == '__main__':
    cProfile.run('most_frequent_item_count_1(collection)')
    cProfile.run('most_frequent_item_count_2(collection)')
    cProfile.run('most_frequent_item_count_3(collection)')

    start_time = time.time()
    most_frequent_item_count_1(collection)
    end_time = time.time()
    print('first approach timestamp', end_time - start_time)

    start_time = time.time()
    most_frequent_item_count_2(collection)
    end_time = time.time()
    print('second approach timestamp', end_time - start_time)

    start_time = time.time()
    most_frequent_item_count_3(collection)
    end_time = time.time()
    print('third approach timestamp', end_time - start_time)
