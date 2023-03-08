// Move the first letter of each word to the end of it, then add "ay" to the end of the word.
// Leave punctuation marks untouched.


/* Solution one */
// time complexity of the algorithm is O(n)
export const pigItOne = (str) => {
    return str.replace(/\b(\w)(\w*)\b/g, (match, firstChar, restChars) => {
        return restChars + firstChar + 'ay';
    });
}

/* Solution one */
// time complexity of the algorithm is O(n)
// improved the performance of this algorithm by doing the separation and concatenation in a single loop
export const pigItTwo = (str) => {
    const words = str.split(' ');
    const pigWords = [];

    for (let i = 0; i < words.length; i++) {
        const word = words[i];
        const firstChar = word.charAt(0);
        const restChars = word.slice(1);
        const pigWord = restChars + firstChar + 'ay';

        pigWords.push(pigWord);
    }

    return pigWords.join(' ');
}
