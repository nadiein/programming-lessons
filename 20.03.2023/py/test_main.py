import main


def test_order_weight():
    test_cases = (
        ('103 123 4444 99 2000', '2000 103 123 4444 99'),
        ('2000 10003 1234000 44444444 9999 11 11 22 123', '11 11 2000 10003 22 123 1234000 44444444 9999'),
        ('', '')
    )

    for inputed, expected in test_cases:
        # First approach
        assert main.order_weight_one(inputed) == expected
        # Second approach
        assert main.order_weight_two(inputed) == expected
        # Third approach
        assert main.order_weight_three(inputed) == expected
        # Fourth approach
        assert main.order_weight_four(inputed) == expected
