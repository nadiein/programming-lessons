import { formatDuration } from './main';


describe('Test format time duration method that returns formated human readable format from number of seconds', () => {
    const test = [
        [1, '1 second'],
        [62, '1 minute and 2 seconds'],
        [120, '2 minutes'],
        [3600, '1 hour'],
        [3662, '1 hour, 1 minute and 2 seconds']
    ];

    it('test format seconds duration', () => {
        for ( const [input, expected] of test ) {
            expect(formatDuration(input)).toEqual(expected);
        }
    });
})
