import main
import tests


# First approach
def test_last_digit():

    for x, y in tests.test_cases:
        # First approach
        assert main.last_digit(x) == y
