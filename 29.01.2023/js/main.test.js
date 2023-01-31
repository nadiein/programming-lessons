import { RomanNumerals } from './main';


describe('Test RomanNumerals class that call toRoman method and return roman number', () => {
    const testsToRoman = [
        [1000, 'M'],
        [4, 'IV'],
        [1, 'I'],
        [1990, 'MCMXC'],
        [2008, 'MMVIII']
    ];

    const testsFromRoman = [
        ['XXI', 21],
        ['I', 1],
        ['IV', 4],
        ['MMVIII', 2008],
        ['MDCLXVI', 1666]
    ];

    it('test to roman method', () => {
        for ( const [input, expected] of testsToRoman ) {
            expect(RomanNumerals.toRoman(input)).toBe(expected);
        }
    });

    it('test from roman method', () => {
        for ( const [input, expected] of testsFromRoman ) {
            expect(RomanNumerals.fromRoman(input)).toBe(expected);
        }
    });
})
