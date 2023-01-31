import { permutations } from './main';


describe('Test permutations method that returns permutations of passed string', () => {
    const test = [
        ['a', ['a']],
        ['ab', ['ab', 'ba']],
        ['aabb', ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']],
    ];

    it('test permutations', () => {
        for ( const [input, expected] of test ) {
            expect(permutations(input)).toEqual(expected);
        }
    });
})
