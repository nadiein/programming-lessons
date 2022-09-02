const createPhoneNumber = require('./main');


const test1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
const test2 = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1];
const test3 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0];
const test4 = [0, 2, 3, 0, 5, 6, 0, 8, 9, 0];
const test5 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0];

test('format [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] to equal (123) 456-7890', () => {
    expect(createPhoneNumber(test1)).toBe('(123) 456-7890')
})

test('format [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] to equal (111) 111-1111', () => {
    expect(createPhoneNumber(test2)).toBe('(111) 111-1111')
})

test('format [1, 2, 3, 4, 5, 6, 7, 8, 9, 0] to equal (123) 456-7890', () => {
    expect(createPhoneNumber(test3)).toBe('(123) 456-7890')
})

test('format [0, 2, 3, 0, 5, 6, 0, 8, 9, 0] to equal (023) 056-0890', () => {
    expect(createPhoneNumber(test4)).toBe('(023) 056-0890')
})

test('format [0, 0, 0, 0, 0, 0, 0, 0, 0, 0] to equal (000) 000-0000', () => {
    expect(createPhoneNumber(test5)).toBe('(000) 000-0000')
})
