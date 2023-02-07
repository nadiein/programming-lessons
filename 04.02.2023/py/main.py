# Write a function that will solve a 9x9 Sudoku puzzle.
# The function will take one argument consisting of the 2D puzzle array, with the value 0
# representing an unknown square and return the solved puzzle as a 2d array of 9 x 9.

# The Sudokus tested against your function will be "easy"
# (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and
# can be solved with a brute-force approach.

# For Sudoku rules, see the Wikipedia article.


class WrongType(Exception):
    pass

# Solution one
def sudoku(puzzle):
    for i in range(9):
        for j in range(9):
            if puzzle[i][j] == 0:
                for num in range(1,10):
                    if is_valid(puzzle, i, j, num):
                        puzzle[i][j] = num
                        solution = sudoku(puzzle)
                        if solution:
                            return solution
                        puzzle[i][j] = 0
                return None
    return puzzle

def is_valid(puzzle, row, col, num):
    for i in range(9):
        if puzzle[row][i] == num or puzzle[i][col] == num:
            return False

    row_start = (row//3)*3
    col_start = (col//3)*3
    for i in range(3):
        for j in range(3):
            if puzzle[row_start+i][col_start+j] == num:
                return False
    return True


import cProfile
import time
from timeit import default_timer as timer


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
