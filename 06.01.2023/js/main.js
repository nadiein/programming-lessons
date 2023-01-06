/*
    Complete the function to find the count of the most frequent item of an array. You can assume that input is an array of integers. For an empty array return 0
*/

/* First solution: the easiest one */
export const mostFrequentItemCount1 = (collection) => {
    // Create an object to store the count of each number
    const counts = {};

    // Initialize the most frequent count to 0
    let mostFrequentCount = 0;

    // Iterate through the array and count the number of occurrences of each number
    for (const num of collection) {
        counts[num] = (counts[num] || 0) + 1;

        // Update the most frequent count if necessary
        if (counts[num] > mostFrequentCount) {
            mostFrequentCount = counts[num];
        }
    }

    // Return the most frequent count
    return mostFrequentCount;
}

/* Second solution: using Set and filter method */
export const mostFrequentItemCount2 = (collection) => {
    // Return 0 for an empty array
    if (collection.length === 0) {
        return 0;
    }

    // Create a set of unique numbers in the array
    const uniqueNumbers = new Set(collection);

    // Use the map method to create a new array of counts for each unique number
    const counts = Array.from(uniqueNumbers).map(num => {
        return {
            num: num,
            count: collection.filter(x => x === num).length
        };
    });

    // Use the reduce method to find the object with the highest count
    const mostFrequent = counts.reduce((acc, curr) => {
        return (curr.count > acc.count) ? curr : acc;
    });

    // Return the count of the most frequent number
    return mostFrequent.count;
}

/* Third solution: using for each method. The fastest one. Do not create additional array as reduce does. */
export const mostFrequentItemCount3 = (collection) => {
    // Return 0 for an empty array
    if (collection.length === 0) {
        return 0;
    }

    // Create an object to store the count of each number
    const counts = {};

    // Initialize the most frequent count to 0
    let mostFrequentCount = 0;

    // Count the number of occurrences of each number
    collection.forEach(num => {
        counts[num] = (counts[num] || 0) + 1;

        // Update the most frequent count if necessary
        if (counts[num] > mostFrequentCount) {
            mostFrequentCount = counts[num];
        }
    });

    // Return the most frequent count
    return mostFrequentCount;
}
