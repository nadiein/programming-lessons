import { orderWeightOne, orderWeightTwo, orderWeightThree } from './main';


describe('Test order weights', () => {
    it('test cases', () => {
        const testCases = [
            ['103 123 4444 99 2000', '2000 103 123 4444 99'],
            ['2000 10003 1234000 44444444 9999 11 11 22 123', '11 11 2000 10003 22 123 1234000 44444444 9999'],
            ['', '']
        ]

        for ( const [input, expected] of testCases ) {
            /* Solution one */
            expect(orderWeightOne(input)).toEqual(expected)
            /* Solution two */
            expect(orderWeightTwo(input)).toEqual(expected)
            /* Solution three */
            expect(orderWeightThree(input)).toEqual(expected)
        }
    });
})
