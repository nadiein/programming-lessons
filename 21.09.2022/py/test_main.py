import main


test_points_1 = ( (2, 2), (2, 8), (5, 5), (6, 3), (6, 7), (7, 4), (7, 9) )
test_points_2 = ( (2, 2), (2, 8), (5, 5), (5, 5), (6, 3), (6, 7), (7, 4), (7, 9) )


def test_find_distance():
    assert main.find_distance(1, 1, 1, 1) == 0.0
    assert main.find_distance(9, 6, 2, 8) == 7.3
    assert main.find_distance(5, 5, 5, 5) == 0.0
    assert main.find_distance(6, 3, 7, 4) == 1.4

def test_find_closest_pairs():
    assert main.find_closest_pairs(test_points_1) == ((6, 3), (7, 4))
    assert main.find_closest_pairs(test_points_2) == ((5, 5), (5, 5))