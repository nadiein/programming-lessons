import { traverseTCPStates } from './main';


describe('Test function that return TCP status depends on input', () => {
    it('test cases', () => {
        const testCases = [
            [['APP_ACTIVE_OPEN','RCV_SYN_ACK','RCV_FIN'], 'CLOSE_WAIT'],
            [['APP_PASSIVE_OPEN',  'RCV_SYN','RCV_ACK'], 'ESTABLISHED'],
            [['APP_ACTIVE_OPEN','RCV_SYN_ACK','RCV_FIN','APP_CLOSE'], 'LAST_ACK'],
            [['APP_ACTIVE_OPEN'], 'SYN_SENT'],
            [['APP_PASSIVE_OPEN','RCV_SYN','RCV_ACK','APP_CLOSE','APP_SEND'], 'ERROR']
        ]

        for ( const [input, expected] of testCases ) {
            expect(traverseTCPStates(input)).toEqual(expected);
        }
    });
})
