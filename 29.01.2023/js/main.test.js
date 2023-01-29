import { RomanNumerals } from './main';


describe('Test RomanNumerals class that call toRoman method and return roman number', () => {
    const testsToRoman = [
        [RomanNumerals.toRoman(1000), 'M'],
        [RomanNumerals.toRoman(4), 'IV'],
        [RomanNumerals.toRoman(1), 'I'],
        [RomanNumerals.toRoman(1990), 'MCMXC'],
        [RomanNumerals.toRoman(2008), 'MMVIII']
    ];

    const testsFromRoman = [
        [RomanNumerals.fromRoman('XXI'), 21],
        [RomanNumerals.fromRoman('I'), 1],
        [RomanNumerals.fromRoman('IV'), 4],
        [RomanNumerals.fromRoman('MMVIII'), 2008],
        [RomanNumerals.fromRoman('MDCLXVI'), 1666]
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
