import { getPins } from './main';


describe('Test get pins method that returns variations of passed pin', () => {
    const test = [
        ['8', ['5', '7', '8', '9', '0']],
        ['11', ['11', '12', '14', '21', '22', '24', '41', '42', '44']],
        ['369',  ['236', '238', '239', '256', '258', '259', '266', '268', '269', '296', '298', '299', '336', '338', '339', '356', '358', '359', '366', '368', '369', '396', '398', '399', '636', '638', '639', '656', '658', '659', '666', '668', '669', '696', '698', '699']]
    ]

    it('test get pins', () => {
        for ( const [input, expected] of test ) {
            expect(getPins(input)).toStrictEqual(expected);
        }
    });
})
