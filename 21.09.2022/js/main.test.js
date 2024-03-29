import {
    findClosestDistance,
    findClosestPairOne,
    findClosestPairTwo
} from './main';


const test_array_1 = [ [2,2],[2,8],[5,5],[6,3],[6,7],[7,4],[7,9] ];
const test_array_2 = [ [2,2],[2,8],[5,5],[5,5],[6,3],[6,7],[7,4],[7,9] ];


describe('Test find closest distance method', () => {
    it('Get float number that represent distance between coordinates from 1, 1, 1, 1 to be equal 0.0', () => {
        expect(findClosestDistance(1, 1, 1, 1)).toEqual(0.0)
    });
    
    it('Get float number that represent distance between coordinates from 9, 6, 2, 8 to be equal 7.3', () => {
        expect(findClosestDistance(9, 6, 2, 8)).toBe(7.3)
    });
    
    it('Get float number that represent distance between coordinates from 5, 5, 5, 5 to be equal 0.0', () => {
        expect(findClosestDistance(5, 5, 5, 5)).toBe(0.0)
    });
    
    it('Get float number that represent distance between coordinates from 6, 3, 7, 4 to be equal 1.4', () => {
        expect(findClosestDistance(6, 3, 7, 4)).toBe(1.4)
    });
})

describe('Test find closest pair method for Solution one', () => {
    it('Get [ [2, 2], [2, 8], [5, 5], [6, 3], [6, 7], [7, 4], [7, 9] ] and return array of closest points [6, 3], [7, 4]', () => {
        expect(findClosestPairOne(test_array_1)).toEqual([[6, 3], [7, 4]])
    });
    it('Get [ [2, 2], [2, 8], [5, 5], [5, 5], [6, 3], [6, 7], [7, 4], [7, 9] ] and return array of closest points [5, 5], [5, 5]', () => {
        expect(findClosestPairOne(test_array_2)).toEqual([[5, 5], [5, 5]])
    })
})

describe('Test find closest pair method for Solution two', () => {
    it('Get [ [2, 2], [2, 8], [5, 5], [6, 3], [6, 7], [7, 4], [7, 9] ] and return array of closest points [6, 3], [7, 4]', () => {
        expect(findClosestPairTwo(test_array_1)).toEqual([[6, 3], [7, 4]])
    });
    it('Get [ [2, 2], [2, 8], [5, 5], [5, 5], [6, 3], [6, 7], [7, 4], [7, 9] ] and return array of closest points [5, 5], [5, 5]', () => {
        expect(findClosestPairTwo(test_array_2)).toEqual([[5, 5], [5, 5]])
    })
})
