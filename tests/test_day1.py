import pytest
from day1 import Day1


def test_day1_part1():
    d1 = Day1('../data/day1_input.txt')
    assert d1.day1_part1() == 55834, "Day 1, part1 shows unexpected results."


def test_day1_part2():
    d1 = Day1('../data/day1_input.txt')
    assert d1.day1_part2() == 53221, "Day 1, part2 shows unexpected results."
