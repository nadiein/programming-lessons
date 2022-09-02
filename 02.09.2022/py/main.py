# Write a function that accepts an array of 10 integers (between 0 and 9),
# that returns a string of those numbers in # the form of a phone number.
# Example:
# create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"

import re


# First case, we've used in here regular expression
# with backreference for replacement
def create_phone_number_1(numbers):
    nums = ''.join(map(str, numbers))
    pattern = r'^(\d{3})(\d{3})(\d{4})$'
    repl = r'(\1) \2-\3'
    return re.sub(pattern, repl, nums)


def create_phone_number_2(numbers):
    return '({}{}{}) {}{}{}-{}{}{}{}'.format(*numbers)


# Third case, we've used in here old format way
def create_phone_number_3(numbers):
    numbers_str = ''.join(map(str, numbers))
    return '(%s) %s-%s'%(numbers_str[:3], numbers_str[3:6], numbers_str[6:])


if __name__ == '__main__':
    create_phone_number_1([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    create_phone_number_2([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
    create_phone_number_3([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])
