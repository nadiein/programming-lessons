// Write a function that, given a string of text (possibly with punctuation and line-breaks), returns an array of the top-3 most occurring words, in descending order of the number of occurrences.

// Assumptions:
// A word is a string of letters (A to Z) optionally containing one or more apostrophes (') in ASCII.
// Apostrophes can appear at the start, middle or end of a word ('abc, abc', 'abc', ab'c are all valid)
// Any other characters (e.g. #, \, / , . ...) are not part of a word and should be treated as whitespace.
// Matches should be case-insensitive, and the words in the result should be lowercased.
// Ties may be broken arbitrarily.
// If a text contains fewer than three unique words, then either the top-2 or top-1 words should be returned, or an empty array if a text contains no words.
// Examples:
// top_3_words("In a village of La Mancha, the name of which I have no desire to call to
// mind, there lived not long since one of those gentlemen that keep a lance
// in the lance-rack, an old buckler, a lean hack, and a greyhound for
// coursing. An olla of rather more beef than mutton, a salad on most
// nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
// on Sundays, made away with three-quarters of his income.")
// # => ["a", "of", "on"]

// top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
// # => ["e", "ddd", "aa"]

// top_3_words("  //wont won't won't")
// # => ["won't", "wont"]

// 1. Avoid creating an array whose memory footprint is roughly as big as the input text.
// 2. Avoid sorting the entire array of unique words.


/* Solution one */
// time complexity of O(n log n) due to the sorting of the words array,
// where n is the number of unique words in the input text. In the worst case,
// where all words are unique, the algorithm will need to sort all n words.
// This may not be optimal for large input texts.
export const topThreeWordsOne = (text) => {
    // create a regular expression to match words
    const regex = /[a-z]+('[a-z]+)?/gi;

    // count the frequency of each word
    const counts = {};
    let match;

    while ((match = regex.exec(text))) {
        const word = match[0].toLowerCase();
        counts[word] = (counts[word] || 0) + 1;
    }

    // sort the words by frequency
    const words = Object.keys(counts);
    words.sort((a, b) => counts[b] - counts[a]);

    // return the top-3 most occurring words
    return words.slice(0, 3);
}

// Solution two
// time complexity of O(n), where n is the number of words in the input text.
// The idea is to use a hash table to count the frequency of each word,
//and then use a min heap to keep track of the top-3 most occurring words.
export const topThreeWordsTwo = (text) => {
    // create a hash table to count the frequency of each word
    const counts = {};

    text.toLowerCase().split(/[^\w']+/).forEach(word => {
        if (word !== '' && !/^'+$/.test(word)) {
            counts[word] = (counts[word] || 0) + 1;
        }
    });

    // create a min heap to keep track of the top-3 most occurring words
    const heap = new MinHeap();

    Object.keys(counts).forEach(word => {
        heap.insert({
            word,
            count: counts[word]
        });

        if (heap.size() > 3) {
            heap.extractMin();
        }
    });

    // return the top-3 most occurring words in descending order
    const result = [];

    while (!heap.isEmpty()) {
        result.unshift(heap.extractMin().word);
    }

    return result;
}

class MinHeap {
    constructor() {
        this.heap = [];
    }

    size() {
        return this.heap.length;
    }

    isEmpty() {
        return this.heap.length === 0;
    }

    insert(value) {
        this.heap.push(value);
        this.bubbleUp(this.heap.length - 1);
    }

    extractMin() {
        const min = this.heap[0];
        const last = this.heap.pop();

        if (!this.isEmpty()) {
            this.heap[0] = last;
            this.bubbleDown(0);
        }

        return min;
    }

    bubbleUp(index) {
        const parentIndex = Math.floor((index - 1) / 2);

        if (index > 0 && this.heap[parentIndex].count > this.heap[index].count) {
            this.swap(index, parentIndex);
            this.bubbleUp(parentIndex);
        }
    }

    bubbleDown(index) {
        const leftChildIndex = 2 * index + 1;
        const rightChildIndex = 2 * index + 2;
        let minIndex = index;

        if (leftChildIndex < this.heap.length &&
            this.heap[leftChildIndex].count < this.heap[minIndex].count) {
            minIndex = leftChildIndex;
        }

        if (rightChildIndex < this.heap.length &&
            this.heap[rightChildIndex].count < this.heap[minIndex].count) {
            minIndex = rightChildIndex;
        }

        if (index !== minIndex) {
            this.swap(index, minIndex);
            this.bubbleDown(minIndex);
        }
    }

    swap(i, j) {
        const temp = this.heap[i];
        this.heap[i] = this.heap[j];
        this.heap[j] = temp;
    }
}
