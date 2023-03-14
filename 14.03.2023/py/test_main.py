import main


def test_choose_best_sum():
    xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]

    test_cases = (
        ([230, 4], 230),
        ([430, 5], 430),
        ([430, 8], None)
    )

    for x, y in test_cases:
        # First approach
        assert main.choose_best_sum_one(x[0], x[1], xs) == y
        # Second approach
        assert main.choose_best_sum_two(x[0], x[1], xs) == y
