import main


def test_count_patterns_from():
    assert main.count_patterns_from('a', 10) == 0
    assert main.count_patterns_from('b', 1) == 1
    assert main.count_patterns_from('i', 14) == 0
    assert main.count_patterns_from('e', 2) == 8
    assert main.count_patterns_from('b', 2) == 5
    assert main.count_patterns_from('e', 4) == 256
