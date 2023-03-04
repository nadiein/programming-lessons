import main


# First approach
def test_sum_of_squares():
    test_cases = (
        (15, 4),
        (16, 1),
        (17, 2),
        (18, 2),
        (19, 3)
    )

    for x, y in test_cases:
        # First approach
        assert main.sum_of_squares(x) == y
