import { cutLog } from './main';


describe('Test cutLog', () => {
    it('test cases', () => {
        const p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 32, 35, 39, 43, 43, 45, 49, 50, 54, 57, 60, 65, 68, 70, 74, 80, 81, 84, 85, 87, 91, 95, 99, 101, 104, 107, 112, 115, 116, 119]
        const testCases = [
            [[p, 1], 1],
            [[p, 5], 13],
            [[p, 8], 22],
            [[p, 10], 30],
            [[p, 22], 65],
            [[p, 35], 105]
        ]

        for ( const [input, expected] of testCases ) {
            expect(cutLog(input[0], input[1])).toEqual(expected)
        }
    });
})
