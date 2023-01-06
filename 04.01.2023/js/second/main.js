/*
    Write a function solution  that, given two integers A and B, returns the number of integers from the range [A..B] (ends are included) which can be expressed as the product of two consecutive integers, that is X * (X + 1), for some integer X.
    Write an  algorithm for the following assumptions:
    A and B are integers within the range [1..1000000000];
    A ≤ B;
    Use javascript;
*/

function solution(A, B) {
    if ( A < 0 || A > 1000000000 ) return -1;
    if ( B < 0 || B > 1000000000 ) return -1;
    if ( A > B ) return -1;

    let res = 0;

    for ( let i = 2; i * ( i + 1 ) <= B; i++ ) {

        if ( i * ( i + 1 ) >= A ) {
            res++;
        }
    }

    return res;
}