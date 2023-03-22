import { domainName } from './main';


describe('Test url parser', () => {
    it('test cases', () => {
        const testCases = [
            ['http://google.com', 'google'],
            ['https://google.com', 'google'],
            ['www.xakep.ru', 'xakep'],
            ['https://youtube.com', 'youtube']
        ]

        for ( const [input, expected] of testCases ) {
            /* Solution one */
            expect(domainName(input)).toEqual(expected)
        }
    });
})
