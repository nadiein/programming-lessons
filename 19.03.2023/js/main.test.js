import { rgbOne, rgbTwo, rgbThree, rgbFour, rgbFive } from './main';


describe('Test rgb', () => {
    it('test cases', () => {
        const testCases = [
            [[0, 0, 0], '000000'],
            [[0, 0, -20], '000000'],
            [[300,255,255], 'FFFFFF'],
            [[173,255,47], 'ADFF2F']
        ]

        for ( const [input, expected] of testCases ) {
            /* Solution one */
            expect(rgbOne(input[0], input[1], input[2])).toEqual(expected)
            /* Solution two */
            expect(rgbTwo(input[0], input[1], input[2])).toEqual(expected)
            /* Solution three */
            expect(rgbThree(input[0], input[1], input[2])).toEqual(expected)
            /* Solution four */
            expect(rgbFour(input[0], input[1], input[2])).toEqual(expected)
            /* Solution five */
            expect(rgbFive(input[0], input[1], input[2])).toEqual(expected)
        }
    });
})
