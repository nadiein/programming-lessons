import { lastDigit } from './main';
import { testCases } from './tests';


describe('Test last digit method that should return last (decimal) digit of x1 ^ (x2 ^ (x3 ^ (... ^ xn)))', () => {
    it('last digit test cases', () => {
        for ( const [input, expected] of testCases ) {
            expect(lastDigit(input)).toEqual(expected);
        }
    });
})
