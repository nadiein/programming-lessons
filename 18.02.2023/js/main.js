// For a given list [x1, x2, x3, ..., xn] compute the last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn))).

// E. g., with the input [3, 4, 2], your code should return 1 because 3 ^ (4 ^ 2) = 3 ^ 16 = 43046721.

// Beware: powers grow incredibly fast. For example, 9 ^ (9 ^ 9) has more than 369 millions of digits. lastDigit has to deal with such numbers efficiently.

// Corner cases: we assume that 0 ^ 0 = 1 and that lastDigit of an empty list equals to 1.


/* Solution one */
export const lastDigit = (arr) => {
    if (arr.length === 0) {
        return 1;
    }

    let exp = 1;

    for (let i = arr.length - 1; i >= 0; i--) {
        let base = arr[i] % 10;
        exp = Math.pow(base, exp);
        exp %= 10;
    }

    return exp;
}
