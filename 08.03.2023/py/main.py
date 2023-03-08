# Write an algorithm that takes an array and moves all of the zeros to the end,
# preserving the order of the other elements.


class WrongType(Exception):
    pass

# Solution one
# time complexity of the algorithm is O(n) because it iterates over the input list once,
# and the two subsequent for-loops also iterate over the input list once. Therefore, the overall time complexity is O(n).
import re

def pig_it_one(text):
    # Define regular expression to match words
    word_pattern = re.compile(r'\b(\w)(\w*)\b')
    
    # Use regular expression substitution to apply Pig Latin transformation
    return word_pattern.sub(r'\2\1ay', text)

# Solution two
# eliminated the second for-loop, resulting in a more efficient O(n) time complexity
def pig_it_two(text):
    # Split input string into words and apply Pig Latin transformation to each word
    words = text.split()
    pig_words = [word[1:] + word[0] + 'ay' if word.isalpha() else word for word in words]
    
    # Join transformed words back into a string
    return ' '.join(pig_words)


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('pig_it_one("Pig latin is cool")')
    cProfile.run('pig_it_two("Pig latin is cool")')

    start_time = time.time()
    pig_it_one('Pig latin is cool')
    pig_it_two('Pig latin is cool')
    end_time = time.time()

    print('', end_time - start_time)
