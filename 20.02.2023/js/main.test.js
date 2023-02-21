import { solution } from './main';


describe('Test function that strips all text that follows any of a set of comment markers passed in any whitespace at the end of the line should also be stripped out.', () => {
    it('test cases', () => {
        const testCases = [
            [['apples, plums % and bananas\npears\noranges !applesauce', ['%', '!']], 'apples, plums\npears\noranges'],
            [['Q @b\nu\ne -e f g', ['@', '-']], 'Q\nu\ne']
        ]

        for ( const [input, expected] of testCases ) {
            expect(solution(input[0], input[1])).toEqual(expected);
        }
    });
})
