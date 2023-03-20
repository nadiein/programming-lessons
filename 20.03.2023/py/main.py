# Given a string with the weights of FFC members in normal order,
# give this string ordered by "weights" of these numbers


class WrongType(Exception):
    pass

# Solution one
def weight(num):
    return sum(int(digit) for digit in str(num))

def order_weight_one(strng):
    nums = strng.split()
    nums.sort(key=lambda num: (weight(num), num))

    return ' '.join(nums)

# Solution two
def order_weight_two(strng):
    nums = strng.split()
    weight_dict = {num: sum(int(digit) for digit in num) for num in nums}
    sorted_nums = sorted(nums, key=lambda num: (weight_dict[num], num))

    return ' '.join(sorted_nums)

# Solution three
def order_weight_three(strng):
    nums = strng.split()

    def weight(num):
        return sum(int(digit) for digit in num)

    sorted_nums = sorted(nums, key=lambda num: (weight(num), num))

    return ' '.join(sorted_nums)

# Solution four
def order_weight_four(strng):
    nums = strng.split()
    weighted_nums = [(num, sum(int(digit) for digit in num)) for num in nums]
    sorted_nums = [num[0] for num in sorted(weighted_nums, key=lambda num: (num[1], num[0]))]

    return ' '.join(sorted_nums)


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('order_weight_one("103 123 4444 99 2000")')
    cProfile.run('order_weight_two("103 123 4444 99 2000")')
    cProfile.run('order_weight_three("103 123 4444 99 2000")')
    cProfile.run('order_weight_four("103 123 4444 99 2000")')

    start_time = time.time()
    order_weight_one('103 123 4444 99 2000')
    order_weight_two('103 123 4444 99 2000')
    order_weight_three('103 123 4444 99 2000')
    order_weight_four('103 123 4444 99 2000')
    end_time = time.time()

    print('', end_time - start_time)
