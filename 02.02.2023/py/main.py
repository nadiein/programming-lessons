# Convert a string into an integer. The strings simply represent the numbers in words.
# Examples:
#     "one" => 1
#     "twenty" => 20
#     "two hundred forty-six" => 246
#     "seven hundred eighty-three thousand nine hundred and nineteen" => 783919

# Additional Notes:
#     The minimum number is "zero" (inclusively)
#     The maximum number, which must be supported is 1 million (inclusively)
#     The "and" in e.g. "one hundred and twenty-four" is optional, in some cases it's present and in others it's not
#     All tested numbers are valid, you don't need to validate them


class WrongType(Exception):
    pass

# Solution one
def parseInt(string):
    words = {
        'zero': 0,
        'one': 1,
        'two': 2,
        'three': 3,
        'four': 4,
        'five': 5,
        'six': 6,
        'seven': 7,
        'eight': 8,
        'nine': 9,
        'ten': 10,
        'eleven': 11,
        'twelve': 12,
        'thirteen': 13,
        'fourteen': 14,
        'fifteen': 15,
        'sixteen': 16,
        'seventeen': 17,
        'eighteen': 18,
        'nineteen': 19,
        'twenty': 20,
        'thirty': 30,
        'forty': 40,
        'fifty': 50,
        'sixty': 60,
        'seventy': 70,
        'eighty': 80,
        'ninety': 90,
        'hundred': 100,
        'thousand': 1000,
        'million': 1000000
    }

    num_list = string.replace('-', ' ').split()
    res = 0
    curr = 0
    thousands = 0

    for i in range(len(num_list)):
        if num_list[i] == 'and':
            continue

        if num_list[i] in words:
            if num_list[i] == 'hundred':
                curr *= 100
            elif num_list[i] == 'thousand':
                thousands = curr * 1000
                curr = 0
            elif num_list[i] == 'million':
                res += (curr + thousands) * 1000000
                curr = thousands = 0
            else:
                curr += words[num_list[i]]

    return res + curr + thousands


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('parseInt("one")')
    cProfile.run('parseInt("two hundred forty-six")')

    start_time = time.time()
    parseInt('two hundred forty-six')
    end_time = time.time()
    print('', end_time - start_time)
