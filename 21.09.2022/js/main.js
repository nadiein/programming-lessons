// Given a number of points on a plane, your task is to find two points
// with the smallest distance between them in linearithmic O(n log n) time.
// Example:
//     1  2  3  4  5  6  7  8  9
//   1  
//   2    . A
//   3                . D
//   4                   . F       
//   5             . C
//   6              
//   7                . E
//   8    . B
//   9                   . G


export const findClosestDistance = (x1, y1, x2, y2) => {
    return parseFloat(Math.sqrt( (x2 - x1)**2 + (y2 - y1)**2 ).toFixed(1))
}

export const findClosestPair = (points) => {

    const res = []

    for (let i = 0; i < points.length; i++) {
        for (let y = i + 1; y < points.length; y++) {
            const distance = findClosestDistance(points[i][0], points[i][1], points[y][0], points[y][1]);

            if (Number(distance) == 0.0) return [points[i], points[y]];

            const obj = {
                'index': i,
                'sub_index': y,
                'distance': distance
            };

            res.push(obj);
        }
    }

    const minVal = Math.min(...res.map(item => item['distance']));
    const index = res.map(item => item['distance']).indexOf(minVal);

    const pointIndex = res[index]['index'];
    const pointSubIndex = res[index]['sub_index'];

    return [points[pointIndex], points[pointSubIndex]];
}

const points = [
    [2,2], // A
    [2,8], // B
    [5,5], // C
    [6,3], // D
    [6,7], // E
    [7,4], // F
    [7,9]  // G
]

findClosestPair(points)
