import main


# First approach
def test_format_duration():
    cases = (
        (1, '1 second'),
        (62, '1 minute and 2 seconds'),
        (120, '2 minutes'),
        (3600, '1 hour'),
        (3662, '1 hour, 1 minute and 2 seconds')
    );

    for x, y in cases:
        # First approach
        assert main.format_duration(x) == y
