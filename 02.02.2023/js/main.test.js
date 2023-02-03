import { parseInt } from './main';


describe('Test format time duration method that returns formated human readable format from number of seconds', () => {
    const test = [
        ['one', 1],
        ['twenty', 20],
        ['two hundred forty-six', 246],
        ['one million', 1000000],
        ['sixty thousand forty-two', 60042]
    ];

    it('test format seconds duration', () => {
        for ( const [input, expected] of test ) {
            expect(parseInt(input)).toEqual(expected);
        }
    });
})
