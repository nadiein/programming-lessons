import main


# First approach
def test_parseInt():
    cases = (
        ('one', 1),
        ('twenty', 20),
        ('two hundred forty-six', 246),
        ('one million', 1000000),
        ('sixty thousand forty-two', 60042)
    );

    for x, y in cases:
        # First approach
        assert main.parseInt(x) == y
