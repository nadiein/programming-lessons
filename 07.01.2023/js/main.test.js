import { makeReadable } from './main';


describe('Test time conversion from seconds to readble format', () => {
    it('Test solution one', () => {
        expect(makeReadable(0)).toBe('00:00:00');
        expect(makeReadable(5)).toBe('00:00:05');
        expect(makeReadable(60)).toBe('00:01:00');
        expect(makeReadable(86399)).toBe('23:59:59');
        expect (makeReadable(359999)).toBe('99:59:59');
    })
})
