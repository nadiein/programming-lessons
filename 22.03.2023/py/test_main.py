import main


def test_domain_name():
    test_cases = (
        ('http://google.com', 'google'),
        ('https://google.com', 'google'),
        ('www.xakep.ru', 'xakep'),
        ('https://youtube.com', 'youtube')
    )

    for inputed, expected in test_cases:
        # First approach
        assert main.domain_name_one(inputed) == expected
        # Second approach
        assert main.domain_name_two(inputed) == expected
        # Third approach
        assert main.domain_name_three(inputed) == expected
        # Fourth approach
        assert main.domain_name_four(inputed) == expected
