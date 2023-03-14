// Given two strings s1 and s2, we want to visualize how different the two strings are.
// We will only take into account the lowercase letters (a to z).
// First let us count the frequency of each lowercase letters in s1 and s2.


/* Solution one */
// time complexity of the algorithm is O(nlogn), where n is the number of unique lowercase
// letters in the two input strings combined.
export const mix = (s1, s2) => {
    const alphabets = "abcdefghijklmnopqrstuvwxyz";
    const count1 = {},
        count2 = {},
        result = [];

    for (let i = 0; i < alphabets.length; i++) {
        const letter = alphabets[i];
        count1[letter] = s1.split(letter).length - 1;
        count2[letter] = s2.split(letter).length - 1;
    }

    for (let i = 0; i < alphabets.length; i++) {
        const letter = alphabets[i];
        const countInS1 = count1[letter];
        const countInS2 = count2[letter];

        if (countInS1 > 1 || countInS2 > 1) {
            if (countInS1 > countInS2) {
                result.push(`1:${letter.repeat(countInS1)}`);
            } else if (countInS1 < countInS2) {
                result.push(`2:${letter.repeat(countInS2)}`);
            } else {
                result.push(`=:${letter.repeat(countInS1)}`);
            }
        }
    }

    result.sort((a, b) => {
        if (b.length !== a.length) {
            return b.length - a.length;
        }
        return a.charCodeAt(0) - b.charCodeAt(0) || a.localeCompare(b);
    });

    return result.join('/');
}