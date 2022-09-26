const findClosestDistance = require('./main');
const findClosestPair = require('./main');


const test_array_1 = [ [2,2],[2,8],[5,5],[6,3],[6,7],[7,4],[7,9] ];
const test_array_2 = [ [2,2],[2,8],[5,5],[5,5],[6,3],[6,7],[7,4],[7,9] ];


test('Get float number that represent distance between coordinates from 1, 1, 1, 1 to be equal 0.0', () => {
    expect(findClosestDistance(1, 1, 1, 1)).toBe(0.0)
});

// test('Get float number that represent distance between coordinates from 9, 6, 2, 8 to be equal 0.0', () => {
//     expect(findClosestDistance(9, 6, 2, 8)).toBe(7.3)
// });

// test('Get float number that represent distance between coordinates from 5, 5, 5, 5 to be equal 0.0', () => {
//     expect(findClosestDistance(5, 5, 5, 5)).toBe(0.0)
// });

// test('Get float number that represent distance between coordinates from 6, 3, 7, 4 to be equal 0.0', () => {
//     expect(findClosestDistance(6, 3, 7, 4)).toBe(1.4)
// });

// test('Get [ [2, 2], [2, 8], [5, 5], [6, 3], [6, 7], [7, 4], [7, 9] ] and return array of closest points [6, 3], [7, 4]', () => {
//     expect(findClosestPair(test_array_1)).toStrictEqual([[6, 3], [7, 4]])
// });

// test('Get [ [2, 2], [2, 8], [5, 5], [5, 5], [6, 3], [6, 7], [7, 4], [7, 9] ] and return array of closest points [5, 5], [5, 5]', () => {
//     expect(findClosestPair(test_array_2)).toStrictEqual([[5, 5], [5, 5]])
// })
