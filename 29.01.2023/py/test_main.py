import main


# First approach
def test():
    # First approach
    cases_to = (
        (1000, 'M'),
        (4, 'IV'),
        (1, 'I'),
        (1990, 'MCMXC'),
        (2008, 'MMVIII')
    );

    cases_from = (
        ('XXI', 21),
        ('I', 1),
        ('IV', 4),
        ('MMVIII', 2008),
        ('MDCLXVI', 1666)
    );

    for x, y in cases_to:
        assert main.RomanNumerals.toRoman(x) == y

    for x, y in cases_from:
        assert main.RomanNumerals.fromRoman(x) == y
