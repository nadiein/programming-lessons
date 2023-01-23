import main


# First approach
def test_calc():
    # First approach
    cases = (
            ('1 + 1', 2),
            ('8/16', 0.5),
            ('3 -(-1)', 4),
            ('2 + -2', 0),
            ('10- 2- -5', 13),
            ('(((10)))', 10),
            ('3 * 5', 15),
            ('-7 * -(6 / 3)', 14)
        )

    for x, y in cases:
        assert main.calc(x) == y
