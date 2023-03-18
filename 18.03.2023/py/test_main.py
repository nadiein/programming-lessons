import main


def test_cut_log():
    p = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30, 32, 35, 39, 43, 43, 45, 49, 50, 54, 57, 60, 65, 68, 70, 74, 80, 81, 84, 85, 87, 91, 95, 99, 101, 104, 107, 112, 115, 116, 119]
    test_cases = (
        ((p, 1), 1),
        ((p, 5), 13),
        ((p, 8), 22),
        ((p, 10), 30),
        ((p, 22), 65),
        ((p, 35), 105)
    )

    for inputed, expected in test_cases:
        # First approach
        assert main.cut_log(inputed[0], inputed[1]) == expected
