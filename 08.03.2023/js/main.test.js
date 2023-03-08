import { pigItOne, pigItTwo } from './main';


describe('Test function should move the first letter of each word to the end of it, then add "ay" to the end of the word', () => {
    it('test cases', () => {
        const testCases = [
            ['Pig latin is cool', 'igPay atinlay siay oolcay'],
            ['This is my string', 'hisTay siay ymay tringsay']
        ]

        for ( const [input, expected] of testCases ) {
            expect(pigItOne(input)).toEqual(expected);
            expect(pigItTwo(input)).toEqual(expected);
        }
    });
})
