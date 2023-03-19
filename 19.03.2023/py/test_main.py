import main


def test_rgb():
    test_cases = (
        ((0, 0, 0), '000000'),
        ((1, 2, 3), '010203'),
        ((255, 255, 255), 'FFFFFF'),
        ((254, 253, 252), 'FEFDFC'),
        ((-20, 275, 125), '00FF7D')
    )

    for inputed, expected in test_cases:
        # First approach
        assert main.rgb_one(inputed[0], inputed[1], inputed[2]) == expected
        # Second approach
        assert main.rgb_two(inputed[0], inputed[1], inputed[2]) == expected
        # Third approach
        assert main.rgb_three(inputed[0], inputed[1], inputed[2]) == expected
        # Fourth approach
        assert main.rgb_four(inputed[0], inputed[1], inputed[2]) == expected
        # Fifth approach
        assert main.rgb_five(inputed[0], inputed[1], inputed[2]) == expected
