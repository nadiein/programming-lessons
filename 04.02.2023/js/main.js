// Write a function that will solve a 9x9 Sudoku puzzle.
// The function will take one argument consisting of the 2D puzzle array, with the value 0
// representing an unknown square and return the solved puzzle as a 2d array of 9 x 9.

// The Sudokus tested against your function will be "easy"
// (i.e. determinable; there will be no need to assume and test possibilities on unknowns) and
// can be solved with a brute-force approach.

// For Sudoku rules, see the Wikipedia article.


/* Solution one */
export const sudoku = (puzzle) => {
    for (let i = 0; i < 9; i++) {
        for (let j = 0; j < 9; j++) {

            if (puzzle[i][j] === 0) {
                for (let k = 1; k <= 9; k++) {

                    if (isValid(puzzle, i, j, k)) {
                        puzzle[i][j] = k;

                        if (sudoku(puzzle)) {
                            return puzzle;
                        } else {
                            puzzle[i][j] = 0;
                        }
                    }
                }

                return false;
            }
        }
    }

    return puzzle;
}

export const isValid = (puzzle, row, col, num) => {
    for (let i = 0; i < 9; i++) {
        if (puzzle[row][i] === num || puzzle[i][col] === num) {
            return false;
        }
    }

    let sqrt = Math.sqrt(puzzle.length);
    let boxRowStart = row - row % sqrt;
    let boxColStart = col - col % sqrt;

    for (let i = boxRowStart; i < boxRowStart + sqrt; i++) {
        for (let j = boxColStart; j < boxColStart + sqrt; j++) {
            if (puzzle[i][j] === num) {
                return false;
            }
        }
    }

    return true;
}