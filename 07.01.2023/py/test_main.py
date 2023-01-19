import main


# First approach
def test_make_readable():
    # First approach
    assert main.make_readable(0) == '00:00:00'
    assert main.make_readable(5) == '00:00:05'
    assert main.make_readable(60) == '00:01:00'
    assert main.make_readable(86399) == '23:59:59'
    assert main.make_readable(359999) == '99:59:59'
