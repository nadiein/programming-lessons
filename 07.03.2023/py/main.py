# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.


class WrongType(Exception):
    pass

# Solution one
# time complexity of the algorithm is O(n) because it iterates over the input list once,
# and the two subsequent for-loops also iterate over the input list once. Therefore, the overall time complexity is O(n).
def move_zeros_one(lst):
    # Initialize a new list to hold the non-zero elements
    non_zero_lst = []

    # Initialize a variable to keep track of the number of zeros
    zero_count = 0

    # Iterate over the input list and append non-zero elements to the new list
    for elem in lst:
        if elem != 0:
            non_zero_lst.append(elem)
        else:
            zero_count += 1

    # Append zeros to the new list based on the zero count
    for i in range(zero_count):
        non_zero_lst.append(0)

    # Return the new list
    return non_zero_lst

# Solution two
# eliminated the second for-loop, resulting in a more efficient O(n) time complexity
def move_zeros_two(lst):
    # Initialize a variable to keep track of the last non-zero index
    last_non_zero_index = 0

    # Iterate over the input list and swap non-zero elements to the beginning of the list
    for i in range(len(lst)):
        if lst[i] != 0:
            lst[last_non_zero_index], lst[i] = lst[i], lst[last_non_zero_index]
            last_non_zero_index += 1

    # Return the modified list
    return lst


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('move_zeros_one([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])')
    cProfile.run('move_zeros_two([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])')

    start_time = time.time()
    move_zeros_one([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])
    move_zeros_two([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9])
    end_time = time.time()

    print('', end_time - start_time)
