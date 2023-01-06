import {
    mostFrequentItemCount1,
    mostFrequentItemCount2,
    mostFrequentItemCount3
} from './main';


const testArr1 = [3, -1, -1, -1, 2, 3, -1, 3, -1, 2, 4, 9, 3];
const testArr2 = [3, -1, -1];

describe('Test most frequent methods', () => {
    /* First solution */
    it('Find the count of the most frequent item of an array 1 method mostFrequentItemCount1 ', () => {
        expect(mostFrequentItemCount1(testArr1)).toBe(5);
    })

    it('Find the count of the most frequent item of an array 2 method mostFrequentItemCount1 ', () => {
        expect(mostFrequentItemCount1(testArr2)).toBe(2);
    })

    /* Second soulution */
    it('Find the count of the most frequent item of an array 1 method mostFrequentItemCount2 ', () => {
        expect(mostFrequentItemCount2(testArr1)).toBe(5);
    })

    it('Find the count of the most frequent item of an array 2 method mostFrequentItemCount2 ', () => {
        expect(mostFrequentItemCount2(testArr2)).toBe(2);
    })

    /* Third solution */
    it('Find the count of the most frequent item of an array 1 method mostFrequentItemCount3 ', () => {
        expect(mostFrequentItemCount3(testArr1)).toBe(5);
    })

    it('Find the count of the most frequent item of an array 2 method mostFrequentItemCount3 ', () => {
        expect(mostFrequentItemCount3(testArr2)).toBe(2);
    })
})
