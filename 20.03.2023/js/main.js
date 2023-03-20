// Given a string with the weights of FFC members in normal order,
// give this string ordered by "weights" of these numbers


/* Solution one */
export const orderWeightOne = (str) => {
    // Remove leading and trailing whitespaces and split the string into an array
    const arr = str.trim().split(/\s+/);
    
    // Define a function to calculate the weight of a number
    function weight(num) {
        return num.split('').reduce((sum, digit) => sum + parseInt(digit), 0);
    }
    
    // Sort the array of numbers by their weight and then by their string value
    arr.sort((a, b) => {
        const weightA = weight(a);
        const weightB = weight(b);

        if (weightA !== weightB) {
            return weightA - weightB;
        } else {
            return a.localeCompare(b);
        }
    });
    
    // Join the sorted array into a string with a single space between numbers
    return arr.join(' ');
}

/* Solution two */
export const orderWeightTwo = (str) => {
    // Remove leading and trailing whitespaces and split the string into an array
    const arr = str.trim().split(/\s+/);
    
    // Define a function to calculate the weight of a number
    function weight(num) {
        return num.split('').reduce((sum, digit) => sum + parseInt(digit), 0);
    }
    
    // Map each number to an object with its original value and its weight
    const weightArr = arr.map(num => ({ value: num, weight: weight(num) }));
    
    // Sort the array of objects by weight and then by string value
    weightArr.sort((a, b) => {
        if (a.weight !== b.weight) {
            return a.weight - b.weight;
        } else {
            return a.value.localeCompare(b.value);
        }
    });
    
    // Map the sorted array of objects back to an array of values
    const sortedArr = weightArr.map(obj => obj.value);
    
    // Join the sorted array into a string with a single space between numbers
    return sortedArr.join(' ');
}

/* Solution three */
export const orderWeightThree = (str) => {
    // Remove leading and trailing whitespaces and split the string into an array
    const arr = str.trim().split(/\s+/);
    
    // Define a function to calculate the weight of a number
    function weight(num) {
        return num.split('').reduce((sum, digit) => sum + parseInt(digit), 0);
    }
    
    // Reduce the array of numbers to an object with keys as weights and values as arrays of numbers
    const weightObj = arr.reduce((obj, num) => {
        const w = weight(num);
        obj[w] = obj[w] || [];
        obj[w].push(num);
        return obj;
    }, {});
    
    // Sort the arrays of numbers by string value
    Object.values(weightObj).forEach(arr => arr.sort((a, b) => a.localeCompare(b)));
    
    // Sort the keys of the object numerically
    const sortedWeights = Object.keys(weightObj).sort((a, b) => a - b);
    
    // Map the sorted arrays of numbers to a single array and join into a string
    const sortedArr = sortedWeights.flatMap(weight => weightObj[weight]);

    return sortedArr.join(' ');
}
