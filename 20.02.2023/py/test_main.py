import main


# First approach
def test_last_digit():
    test_cases = (
        (('apples, plums % and bananas\npears\noranges !applesauce', ('%', '!')), 'apples, plums\npears\noranges'),
        (('Q @b\nu\ne -e f g', ('@', '-')), 'Q\nu\ne')
    )

    for x, y in test_cases:
        # First approach
        assert main.solution(x[0], x[1]) == y
