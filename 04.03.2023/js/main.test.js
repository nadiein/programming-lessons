import { sumOfSquaresOne, sumOfSquaresTwo } from './main';


describe('Test function that return the length of the smallest list of perfect squares', () => {
    it('test cases', () => {
        const testCases = [
            [15, 4],
            [16, 1],
            [17, 2],
            [18, 2],
            [19, 3]
        ]

        for ( const [input, expected] of testCases ) {
            expect(sumOfSquaresOne(input)).toEqual(expected);
            expect(sumOfSquaresTwo(input)).toEqual(expected);
        }
    });
})
