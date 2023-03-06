import main


def test_triangle():
    test_cases = (
        ('B', 'B'),
        ('GB', 'R'),
        ('RRR', 'R'),
        ('RGBG', 'B'),
        ('RBRGBRB', 'G'),
        ('RBRGBRBGGRRRBGBBBGG', 'G'),
        ('BGRGRBGBRRBBGRBGBBRBRGBRG', 'B'),
        ('GRBGRRRBGRBGRGBRGBRBRGBRRGRBGRGBB', 'R'),
        ('RBGRBGBRGBRBRGGRBBGRBGBRBBGRBGGBRBGBBGRBGBRGRBGRBB', 'G'),
        ('BGBGRBGRRBGRBGGGRBGRGBGRRGGRBGRGRBGBRGBGBGRGBGBGBGRRBRGRRGBGRGBRGRBGRBGRBBGBRGRGRBGRGBRGBBRGGBRBGGRB', 'G')
    )

    for x, y in test_cases:
        # First approach
        assert main.triangle_one(x) == y
        # Second approach
        assert main.triangle_two(x) == y
