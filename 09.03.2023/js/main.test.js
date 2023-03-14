import { mix } from './main';


describe('Test function should move the first letter of each word to the end of it, then add "ay" to the end of the word', () => {
    it('test cases', () => {
        const testCases = [
            [['Are they here', 'yes, they are here'], '2:eeeee/2:yy/=:hh/=:rr'],
            [['Sadus:cpms>orqn3zecwGvnznSgacs','MynwdKizfd$lvse+gnbaGydxyXzayp'], '2:yyyy/1:ccc/1:nnn/1:sss/2:ddd/=:aa/=:zz'],
            [['looping is fun but dangerous', 'less dangerous than coding'], '1:ooo/1:uuu/2:sss/=:nnn/1:ii/2:aa/2:dd/2:ee/=:gg'],
            [[' In many languages', ' there\'s a pair of functions'], '1:aaa/1:nnn/1:gg/2:ee/2:ff/2:ii/2:oo/2:rr/2:ss/2:tt'],
            [['Lords of the Fallen', 'gamekult'], '1:ee/1:ll/1:oo'],
            [['codewars', 'codewars'], ''],
            [['A generation must confront the looming ', 'codewarrs'], '1:nnnnn/1:ooooo/1:tttt/1:eee/1:gg/1:ii/1:mm/=:rr']
        ]

        for ( const [input, expected] of testCases ) {
            expect(mix(input[0], input[1])).toEqual(expected);
        }
    });
})
