import { fib } from './main';


describe('Test function that calculates fib .', () => {
    it('test cases', () => {
        const testCases = [
            [0, 0n],
            [1, 1n],
            [2, 1n],
            [3, 2n],
            [4, 3n],
            [5, 5n],
            [1000, 43466557686937456435688527675040625802564660517371780402481729089536555417949051890403879840079255169295922593080322634775209689623239873322471161642996440906533187938298969649928516003704476137795166849228875n]
        ]

        for ( const [input, expected] of testCases ) {
            expect(fib(input)).toEqual(expected);
        }
    });
})
