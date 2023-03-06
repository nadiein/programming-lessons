import { triangleOne, triangleTwo } from './main';


describe('Test function should return the final colour which would appear in the bottom row as a string', () => {
    it('test cases', () => {
        const testCases = [
            ['B', 'B'],
            ['GB', 'R'],
            ['RRR', 'R'],
            ['RGBG', 'B'],
            ['RBRGBRB', 'G'],
            ['RBRGBRBGGRRRBGBBBGG', 'G'],
            ['BGRGRBGBRRBBGRBGBBRBRGBRG', 'B'],
            ['GRBGRRRBGRBGRGBRGBRBRGBRRGRBGRGBB', 'R'],
            ['RBGRBGBRGBRBRGGRBBGRBGBRBBGRBGGBRBGBBGRBGBRGRBGRBB', 'G'],
            ['BGBGRBGRRBGRBGGGRBGRGBGRRGGRBGRGRBGBRGBGBGRGBGBGBGRRBRGRRGBGRGBRGRBGRBGRBBGBRGRGRBGRGBRGBBRGGBRBGGRB', 'G']
        ]

        for ( const [input, expected] of testCases ) {
            expect(triangleOne(input)).toEqual(expected);
            expect(triangleTwo(input)).toEqual(expected);
        }
    });
})
