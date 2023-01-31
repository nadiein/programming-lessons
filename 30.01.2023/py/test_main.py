import main


# First approach
def test_permutations():
    cases = (
        ('a', ['a']),
        ('ab', ['ab', 'ba']),
        ('aabb', ['aabb', 'abab', 'abba', 'baab', 'baba', 'bbaa']),
    );

    for x, y in cases:
        # First approach
        assert main.permutations_1(x) == sorted(y)
        # Second approach
        assert main.permutations_2(x) == sorted(y)
