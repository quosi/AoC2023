import pytest
from day4 import Day4

@pytest.fixture
def setup():
    data = '../data/day4_input.txt'
    d4 = Day4(data)
    return d4

@pytest.fixture
def data(setup):
    d4 = setup
    return d4.calc_win_cards()

def test_calc_win_cards(setup):
    res = [10, 5, 0, 8, 4, 1, 10, 9, 3, 7, 3, 2, 8, 6, 5, 3, 4, 3, 1, 2,
           0, 0, 10, 10, 10, 6, 3, 1, 5, 3, 6, 0, 2, 7, 3, 7, 2, 8, 2, 1,
           2, 5, 0, 2, 0, 1, 0, 5, 2, 5, 5, 5, 4, 8, 5, 5, 2, 0, 1, 0, 0,
           0, 10, 5, 6, 2, 10, 10, 3, 2, 8, 0, 7, 4, 0, 5, 4, 1, 0, 2, 0,
           0, 10, 8, 1, 3, 0, 10, 1, 8, 5, 6, 2, 6, 4, 1, 4, 0, 2, 0, 0, 10,
           10, 10, 10, 10, 8, 10, 10, 4, 6, 10, 2, 6, 2, 8, 6, 6, 6, 0, 3,
           4, 1, 0, 1, 0, 3, 9, 3, 10, 9, 4, 5, 1, 3, 7, 2, 4, 4, 1, 0, 1,
           0, 10, 5, 10, 4, 10, 3, 5, 7, 3, 6, 0, 3, 6, 5, 0, 3, 0, 0, 0, 0,
           10, 0, 10, 10, 10, 5, 7, 10, 6, 1, 7, 4, 7, 0, 3, 1, 3, 1, 0, 0,
           10, 10, 0, 6, 9, 5, 4, 2, 1, 4, 3, 2, 2, 2, 0, 0]
    d4 = setup
    assert d4.calc_win_cards() == res


def test_day4_part1(setup, data):
    d4, win_cards = setup, data
    assert d4.day4_part1(win_cards) == 18653, "Day 4, part1: Number or cards is inaccurate."


def test_day4_part2(setup, data):
    d4, win_cards = setup, data
    assert d4.day4_part2(win_cards) == 5921508, "Day 4, part2: Number or cards is inaccurate."
