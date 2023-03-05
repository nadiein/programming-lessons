# function should make a list of strings representing all of the ways that can balance n pairs of parentheses

# Examples
#     balanced_parens(0) => [""]
#     balanced_parens(1) => ["()"]
#     balanced_parens(2) => ["()()","(())"]
#     balanced_parens(3) => ["()()()","(())()","()(())","(()())","((()))"]


class WrongType(Exception):
    pass

# Solution one
def balanced_parens_one(n):
    if n == 0:
        return ['']
    elif n == 1:
        return ['()']
    else:
        result = []

        for i in range(n):
            for left in balanced_parens_one(i):
                for right in balanced_parens_one(n - i - 1):
                    result.append('({}){}'.format(left, right))

        return result


import cProfile
import time
from timeit import default_timer as timer


if __name__ == '__main__':
    cProfile.run('balanced_parens_one(["(())","()()"])')

    start_time = time.time()
    balanced_parens_one(['(())', '()()'])
    end_time = time.time()

    print('', end_time - start_time)
