# Complete the function/method (depending on the language) to return true/True
# when its argument is an array that has the same nesting structures and same corresponding
# length of nested arrays as the first array.

# For example:

#  should return true
# [ 1, 1, 1 ].sameStructureAs( [ 2, 2, 2 ] );
# [ 1, [ 1, 1 ] ].sameStructureAs( [ 2, [ 2, 2 ] ] );

#  should return false 
# [ 1, [ 1, 1 ] ].sameStructureAs( [ [ 2, 2 ], 2 ] );
# [ 1, [ 1, 1 ] ].sameStructureAs( [ [ 2 ], 2 ] );

# should return true
# [ [ [ ], [ ] ] ].sameStructureAs( [ [ [ ], [ ] ] ] );

# should return false
# [ [ [ ], [ ] ] ].sameStructureAs( [ [ 1, 1 ] ] );


class WrongType(Exception):
    pass

# Solution one
def same_structure_as(original,other):
    if not isinstance(original, list) or not isinstance(other, list):
        return False

    if len(original) != len(other):
        return False

    for i in range(len(original)):
        if isinstance(original[i], list) and isinstance(other[i], list):
            if not same_structure_as(original[i], other[i]):
                return False
        elif isinstance(original[i], list) or isinstance(other[i], list):
            return False

    return True


case = [1,[1,1]],[2,[2,2]]


if __name__ == '__main__':
    cProfile.run('get_pins(case)')

    start_time = time.time()
    get_pins(case)
    end_time = time.time()

    print('', end_time - start_time)
