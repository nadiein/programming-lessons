import { moveZerosOne, moveZerosTwo } from './main';


describe('Test function should return the final colour which would appear in the bottom row as a string', () => {
    it('test cases', () => {
        const testCases = [
            [[1, 2, 0, 1, 0, 1, 0, 3, 0, 1],
                [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]],
            [[9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9],
            [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]]
        ]

        for ( const [input, expected] of testCases ) {
            expect(moveZerosOne(input)).toEqual(expected);
            expect(moveZerosTwo(input)).toEqual(expected);
        }
    });
})
