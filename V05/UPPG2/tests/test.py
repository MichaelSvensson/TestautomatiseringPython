# importerar funktionen sum_list([]) från modulen uppg2.py

from V05.UPPG2.uppg2 import sum_list

# Testfall testar funktionen sum_list([])
def test_empty_list():
    expected = 0
    actual = sum_list([])
    assert actual == expected


def test_number_list():
    assert sum_list([5]) == 5
    assert sum_list([1, 2, 3]) == 6
    assert sum_list([-1, 0, 1]) == 0
    assert sum_list([10, 8, -18, 4]) == 4