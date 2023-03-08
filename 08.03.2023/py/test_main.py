import main


def test_pig_it():
    test_cases = (
        ('Pig latin is cool', 'igPay atinlay siay oolcay'),
        ('This is my string', 'hisTay siay ymay tringsay')
    )

    for x, y in test_cases:
        # First approach
        assert main.pig_it_one(x) == y
        # Second approach
        assert main.pig_it_two(x) == y
