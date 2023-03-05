import main


def test_balanced_parens():
    test_cases = (
        (0, ['']),
        (1, ['()']),
        (2, ['()()', '(())']),
        (3, ['()()()', '()(())', '(())()', '(()())', '((()))'])
    )

    for x, y in test_cases:
        # First approach
        assert main.balanced_parens_one(x) == y
