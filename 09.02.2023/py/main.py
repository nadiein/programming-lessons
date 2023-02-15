# Alright, detective, one of our colleagues successfully observed our target person,
# Robby the robber. We followed him to a secret warehouse, where we assume to find all
# the stolen stuff. The door to this warehouse is secured by an electronic combination lock.
# Unfortunately our spy isn't sure about the PIN he saw, when Robby entered it.

# The keypad has the following layout:
# ┌───┬───┬───┐
# │ 1 │ 2 │ 3 │
# ├───┼───┼───┤
# │ 4 │ 5 │ 6 │
# ├───┼───┼───┤
# │ 7 │ 8 │ 9 │
# └───┼───┼───┘
#     │ 0 │
#     └───┘
# He noted the PIN 1357, but he also said, it is possible that each of the digits
# he saw could actually be another adjacent digit (horizontally or vertically,
# but not diagonally). E.g. instead of the 1 it could also be the 2 or 4.
# And instead of the 5 it could also be the 2, 4, 6 or 8.

# He also mentioned, he knows this kind of locks. You can enter an unlimited amount of wrong PINs,
# they never finally lock the system or sound the alarm. That's why we can try out all possible (*) variations.

# * possible in sense of: the observed PIN itself and all variations considering the adjacent digits

# Can you help us to find all those variations? It would be nice to have a function, that returns an array or list
# of all variations for an observed PIN with a length of 1 to 8 digits. Write pyhon function getPINs.
# But please note that all PINs, the observed one and also the results, must be strings,
# because of potentially leading '0's.


class WrongType(Exception):
    pass

# Solution one
def get_pins(observed):
    adjacent_digits = {
        '0': ['0', '8'],
        '1': ['1', '2', '4'],
        '2': ['2', '1', '3', '5'],
        '3': ['3', '2', '6'],
        '4': ['4', '1', '5', '7'],
        '5': ['5', '2', '4', '6', '8'],
        '6': ['6', '3', '5', '9'],
        '7': ['7', '4', '8'],
        '8': ['8', '5', '7', '9', '0'],
        '9': ['9', '6', '8']
    }

    variations = set([observed])

    for i in range(len(observed)):
        adjacents = adjacent_digits[observed[i]]

        for adjacent in adjacents:
            variation = observed[:i] + adjacent + observed[i+1:]
            variations.add(variation)

            if len(variation) < len(observed):
                variations |= getPINs(variation)

    return sorted(list(variations))


puzzle = [[5,3,0,0,7,0,0,0,0],
          [6,0,0,1,9,5,0,0,0],
          [0,9,8,0,0,0,0,6,0],
          [8,0,0,0,6,0,0,0,3],
          [4,0,0,8,0,3,0,0,1],
          [7,0,0,0,2,0,0,0,6],
          [0,6,0,0,0,0,2,8,0],
          [0,0,0,4,1,9,0,0,5],
          [0,0,0,0,8,0,0,7,9]]


if __name__ == '__main__':
    cProfile.run('sudoku(puzzle)')

    start_time = time.time()
    sudoku(puzzle)
    end_time = time.time()
    print('', end_time - start_time)
