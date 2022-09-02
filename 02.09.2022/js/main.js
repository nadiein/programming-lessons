/*
    # Write a function that accepts an array of 10 integers (between 0 and 9),
    # that returns a string of those numbers in # the form of a phone number.
    # Example:
    # create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => returns "(123) 456-7890"
*/

/*
    First case, we've used replace function with
    regexp and replace pattern
*/
function createPhoneNumber(numbers) {
    const numbersStr = numbers.join('');
    return numbersStr.replace(/^(\d{3})(\d{3})(\d{4,})$/gi, '($1) $2-$3')
}

createPhoneNumber([1, 2, 3, 4, 5, 6, 7, 8, 9, 0])

module.exports = createPhoneNumber;
