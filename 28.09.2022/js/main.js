// implement a function that returns the number of possible patterns
// starting from a given first point, that have a given length.
// for a function countPatternsFrom(firstPoint, length), the parameter
// firstPoint is a single-character string corresponding to the point in
// the grid (i.e.: 'A') where your patterns start, and the parameter length
// is an integer indicating the number of points (length) every pattern must have.
// For example:
// countPatternsFrom("C", 2), should return the number of patterns starting
// from 'C' that have 2 two points. The return value in this case would be 5,
// because there are 5 possible patterns:
// (C -> B), (C -> D), (C -> E), (C -> F) and (C -> H).
// ---------------///////////////////////////---------------------
// Rules
// In a pattern, the dots/points cannot be repeated: they can only be used once, at most.
// In a pattern, any two subsequent dots/points can only be connected with direct straight lines in either of these ways:
// Horizontally: like (A -> B) in the example pattern image.
// Vertically: like (D -> G) in the example pattern image.
// Diagonally: like (I -> E), as well as (B -> I), in the example pattern image.
// Passing over a point between them that has already been 'used': like (G -> C) passing over E,
// in the example pattern image. This is the trickiest rule. Normally, you wouldn't be able to connect G to C,
// because E is between them, however when E has already been used as ### part the pattern you are tracing,
// you can connect G to C passing over E, because E is ignored, as it was already used once.

// A  B  C
// D  E  F
// G  H  I

// length == 3 ---- E B A
//                  E B C
//                  E D A
//                  E F C
//                  E A B
//                  E C B
//                  E F B
//                  E D B
//                  E F I
//                  E D G
//                  E H G
//                  E H I
//                  E I F
//                  E G D
//                  E G H
//                  E I H
// length == 9 ---- A D G H E B C F I
//                  A D G H I F C B E
//                  A B C F E D G H I
//                  A B C F I H E D G
//                  A B C F I H G D E


export const countPatternsFrom = (firstPoint, length) => {
    if (length === 0) {
        return 0;
    }

    if (length === 1) {
        return 1;
    }

    const connections = {
        'A':['B','D','E'],
        'B':['A','C','D','E','F','I'],
        'C':['B','D','E','F','H'],
        'D':['A','B','C','E','G','H'],
        'E':['A','B','C','D','F','G','H','I'],
        'F':['B','C','E','G','H','I'],
        'G':['D','E','F','H','I'],
        'H':['C','D','E','F','G','I'],
        'I':['B','E','F','G','H']
    }

    const dfs = (point, length, visited) => {
        if (length === 0) {
            return 1;
        }

        let count = 0;

        for (let connection of connections[point]) {
            if (!visited.includes(connection)) {
                count += dfs(connection, length - 1, [...visited,connection]);
            }
        }

        return count;
    }

    return dfs(firstPoint, length - 1, [firstPoint]);
}

countPatternsFrom('A',10)       /* should equal 0 */
countPatternsFrom('A',0)        /* should equal  0 */
countPatternsFrom('E',14)       /* should equal 0 */
countPatternsFrom('B',1)        /* should equal 1 */
countPatternsFrom('C',2)        /* should equal 5 */
countPatternsFrom('E',2)        /* should equal 8 */
