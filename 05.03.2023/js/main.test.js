import { balancedParensOne, balancedParensTwo } from './main';


describe('Test function should make a list of strings representing all of the ways that can balance n pairs of parentheses', () => {
    it('test cases', () => {
        const testCases = [
            [0, ['']],
            [1, ['()']],
            [2, ['()()', '(())']],
            [3, ['()()()', '()(())', '(())()', '(()())', '((()))']]
        ]

        for ( const [input, expected] of testCases ) {
            expect(balancedParensOne(input)).toEqual(expected);
            expect(balancedParensTwo(input)).toEqual(expected);
        }
    });
})
