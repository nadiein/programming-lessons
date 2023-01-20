import main


def test_count_patterns_from():
    assert main.count_patterns_from('A', 10) == 0
    assert main.count_patterns_from('A', 0) == 0
    assert main.count_patterns_from('E', 14) == 0
    assert main.count_patterns_from('B', 1) == 1
    assert main.count_patterns_from('C', 2) == 5
    assert main.count_patterns_from('E', 2) == 8
