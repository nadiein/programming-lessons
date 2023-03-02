# Write a function that, given a string of text (possibly with punctuation and line-breaks),
# returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

# Assumptions:
# A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
# Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
# Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
# Matches should be case-insensitive, and the words in the result should be lowercased.
# Ties may be broken arbitrarily.
# If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
# Examples:
# top_3_words("In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income.")
# # => ["a", "of", "on"]

# top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# # => ["e", "ddd", "aa"]

# top_3_words("  //wont won't won't")
# # => ["won't", "wont"]

# 1. Avoid creating an array whose memory footprint is roughly as big as the input text.
# 2. Avoid sorting the entire array of unique words.


class WrongType(Exception):
    pass

# Solution one
# performance of the provided Python algorithm is O(N log N),
# where N is the length of the input text. This is due to the use of the sorted() function
# to sort the list of words by their frequency.

# The algorithm splits the input text into words using regex, and then uses a Counter to count the frequency of each word.
# Then, it constructs a list of unique words, removes any empty words,
# sorts the list of words by their frequency, and returns the top 3 words.

# The sorted() function has a worst-case time complexity of O(N log N),
# which dominates the overall time complexity of the algorithm. Therefore,
# the algorithm has a time complexity of O(N log N) in the worst case.

# However, the algorithm also uses a significant amount of memory to store the list of words
# and their counts in the Counter. If the input text is very large, this could lead to memory issues.
import re
from collections import Counter

def top_3_words_one(text):
    # Use regex to split the text into words
    words = re.findall(r"[\w']+", text.lower())

    # Use a Counter to count the frequency of each word
    word_counts = Counter(words)

    # Remove single quotes from the list of words
    top_words = [word.strip("'") for word in word_counts.keys()]

    # Remove empty words from the list
    top_words = [word for word in top_words if word]

    # Get the top 3 words, in descending order of frequency
    top_words = sorted(top_words, key=lambda w: (-word_counts[w], w))[:3]

    return top_words

# Solution two
# same performance of the provided Python algorithm is O(N log N),
import re

def top_3_words_two(text):
    words = re.findall(r"[a-z]+(?:'[a-z]+)*", text.lower())
    freq = {}
    for word in words:
        freq[word] = freq.get(word, 0) + 1
    return [word for word, _ in sorted(freq.items(), key=lambda x: x[1], reverse=True)[:3] if word != "''"]


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('top_3_words_one("a a a  b  c c  d d d d  e e e e e")')
    cProfile.run('top_3_words_two("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")')

    start_time = time.time()
    top_3_words_one("  //wont won't won't ")
    top_3_words_two("  '''  ")
    end_time = time.time()

    print('', end_time - start_time)
