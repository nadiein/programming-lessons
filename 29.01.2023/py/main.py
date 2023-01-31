# Create a RomanNumerals class that can convert a roman numeral to and from an integer value.
# Modern Roman numerals are written by expressing each digit separately starting with the left
# most digit and skipping any digit with a value of zero.
# In Roman numerals 1990 is rendered: 1000=M, 900=CM, 90=XC; resulting in MCMXC.
# 2008 is written as 2000=MM, 8=VIII; or MMVIII. 1666 uses each Roman symbol in descending order: MDCLXVI.


class WrongType(Exception):
    pass

# Solution one
class RomanNumerals:

    @staticmethod
    def fromRoman(str):
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        result = 0
        i = 0

        while i < len(str):
            current = map[str[i]]

            if i + 1 < len(str) and map[str[i + 1]] > current:
                result += map[str[i + 1]] - current
                i += 2
            else:
                result += current
                i += 1

        return result

    @staticmethod
    def toRoman(num):
        map = [
            { 'roman': 'M', 'value': 1000 },
            { 'roman': 'CM', 'value': 900 },
            { 'roman': 'D', 'value': 500 },
            { 'roman': 'CD', 'value': 400 },
            { 'roman': 'C', 'value': 100 },
            { 'roman': 'XC', 'value': 90 },
            { 'roman': 'L', 'value': 50 },
            { 'roman': 'XL', 'value': 40 },
            { 'roman': 'X', 'value': 10 },
            { 'roman': 'IX', 'value': 9 },
            { 'roman': 'V', 'value': 5 },
            { 'roman': 'IV', 'value': 4 },
            { 'roman': 'I', 'value': 1 }
        ]

        result = ''

        for item in map:

            while num >= item['value']:
                result += item['roman']
                num -= item['value']

        return result


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('')

    start_time = time.time()
    end_time = time.time()
    print('', end_time - start_time)
