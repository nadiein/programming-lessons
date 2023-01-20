import { countPatternsFrom } from './main';


describe('Test count patterns method', () => {
    it('should return 0 for A, 10', () => {
        expect(countPatternsFrom('A', 10)).toBe(0);
    })
    it('should return 0 for A, 0', () => {
        expect(countPatternsFrom('A', 0)).toBe(0);
    })
    it('should return 0 for E, 14', () => {
        expect(countPatternsFrom('E', 14)).toBe(0);
    })
    it('should return 1 for B, 1', () => {
        expect(countPatternsFrom('B', 1)).toBe(1);
    })
    it('should return 5 for C, 2', () => {
        expect(countPatternsFrom('C', 2)).toBe(5);
    })
    it('should return 8 for E, 2', () => {
        expect(countPatternsFrom('E', 2)).toBe(8);
    })
})
