import { chooseBestSumOne, chooseBestSumTwo } from './main';


describe('Test function should returns the "best" sum ie the biggest possible sum of k distances less than or equal to the given limit t, if that sum exists, or otherwise null', () => {
    it('test cases', () => {
        const tsOne = [50, 55, 56, 57, 58];
        const tsTwo = [50];
        const tsThree = [91, 74, 73, 85, 73, 81, 87];

        // Approach one
        expect(chooseBestSumOne(163, 3, tsOne)).toEqual(163);
        expect(chooseBestSumOne(163, 3, tsTwo)).toEqual(null);
        expect(chooseBestSumOne(230, 3, tsThree)).toEqual(228);
        // Approach two
        expect(chooseBestSumTwo(163, 3, tsOne)).toEqual(163);
        expect(chooseBestSumTwo(163, 3, tsTwo)).toEqual(null);
        expect(chooseBestSumTwo(230, 3, tsThree)).toEqual(228);
    });
})
