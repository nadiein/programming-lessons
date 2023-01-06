/*
    Alice and Bob work in a beautiful orchard. There are N apple trees in the orchard. The apple trees are arranged in a row and they are numbered from 1 to N.
    Alice is planning to collect all the apples from K consecutive trees and Bob is planning to collect all the apples from L consecutive trees. They want to choose two disjoint segments (one consisting of K trees for Alice and the other consisting of L trees for Bob) so as not to disturb each other. What is the maximum number of apples that they can collect?
    Write a function solution(A, K, L): 
    that, given an array A consisting of N integers denoting the number of apples on each apple tree in the row, and integers K and L denoting, respectively, the number of trees that Alice and Bob can choose when collecting, returns the maximum number of apples that can be collected by them, or −1 if there are no such intervals.

    Example test:   ([6, 1, 4, 6, 3, 2, 7, 4], 3, 2) return 24
    Example test:   ([10, 19, 15], 2, 2) return -1
*/

function solution(A, K, L) {
    const numberOfApples = A.length;

    if (K + L > numberOfApples) return -1;

    let max = 0;

    for ( let i = 0; i <= numberOfApples - K - L; i++ ) {
        const applesAlice = A.slice(i, i + K).reduce((sum, x) => sum + x, 0);

        for ( let j = i + K; j <= numberOfApples - L; j++ ) {
            const applesBob = A.slice(j, j + L).reduce((sum, x) => sum + x, 0);

            max = Math.max(max, applesAlice + applesBob);
        }
    }

    return max;
}