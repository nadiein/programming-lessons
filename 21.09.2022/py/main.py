# Given a number of points on a plane, your task is to find two points
# with the smallest distance between them in linearithmic O(n log n) time.
# Example:
#     1  2  3  4  5  6  7  8  9
#   1  
#   2    . A
#   3                . D
#   4                   . F       
#   5             . C
#   6              
#   7                . E
#   8    . B
#   9                   . G


from math import sqrt
import time
from timeit import default_timer as timer
import cProfile


class WrongType(Exception):
    pass

# Solution one
def find_distance(x1:int, y1:int, x2:int, y2:int) -> float:
    return round(sqrt((x2 - x1)**2 + (y2 - y1)**2), 1)

def find_closest_pairs(points:tuple) -> tuple:
    if not isinstance(points, tuple):
        raise WrongType

    l = list()
    count = 1

    for index, point in enumerate(points):
        for sub_index, sub_point in enumerate(points[count:], start=count):
            distance = find_distance(point[0], point[1], sub_point[0], sub_point[1])
            if distance == 0.0:
                return (point, sub_point)
            else:
                d = {
                    'index': index,
                    'sub_index': sub_index,
                    'dis': distance
                }
                l.append(d)
        if count >= len(points):
            count = 1
        count = count + 1

    x = min(l, key=lambda x:x['dis'])['index']
    y = min(l, key=lambda x:x['dis'])['sub_index']

    return (points[x], points[y])

# Solution two
def find_closest_pairs_two(points):
    def distance(p1, p2):
        return sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)

    min_distance = float('inf')
    closest_points = None

    for i in range(len(points)):
        for j in range(i+1, len(points)):
            d = distance(points[i], points[j])

            if d < min_distance:
                min_distance = d
                closest_points = [points[i], points[j]]

    return closest_points

points_one = (
    (2, 2), # A
    (2, 8), # B
    (5, 5), # C
    (6, 3), # D
    (6, 7), # E
    (7, 4), # F
    (7, 9)  # G
)

points_two = [
    (2, 2), # A
    (2, 8), # B
    (5, 5), # C
    (6, 3), # D
    (6, 7), # E
    (7, 4), # F
    (7, 9)  # G
]


if __name__ == '__main__':
    cProfile.run('find_closest_pairs_one(points_one)')
    cProfile.run('find_closest_pairs_two(points_two)')

    start_time = time.time()
    find_closest_pairs_one(points_one)
    end_time = time.time()
    print(end_time - start_time)

    start_time = time.time()
    find_closest_pairs_two(points_two)
