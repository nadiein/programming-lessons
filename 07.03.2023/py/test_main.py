import main


def test_move_zeros():
    test_cases = (
        ([1, 2, 0, 1, 0, 1, 0, 3, 0, 1],
         [1, 2, 1, 1, 3, 1, 0, 0, 0, 0]),
        ([9, 0, 0, 9, 1, 2, 0, 1, 0, 1, 0, 3, 0, 1, 9, 0, 0, 0, 0, 9],
         [9, 9, 1, 2, 1, 1, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    )

    for x, y in test_cases:
        # First approach
        assert main.move_zeros_one(x) == y
        # Second approach
        assert main.move_zeros_two(x) == y
