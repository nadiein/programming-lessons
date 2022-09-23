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


class WrongType(Exception):
    pass

# TODO:// refactor algorithm, it\'s too slow. Should be  O(n log n)
def findClosestPairs(points):
    if isinstance(points) is not tuple:
        raise WrongType

    l = list()
    count = 1
    for index, point in enumerate(points):
        for sub_index, sub_point in enumerate(points[count:], start=count):
            distance = math.sqrt(math.pow(sub_point[0] - point[0], 2) + math.pow(sub_point[1] - point[1], 2))
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
