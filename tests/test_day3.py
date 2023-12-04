import pytest
from day3 import Day3

def test_results_day3():
    data = 'data/day3_input.txt'
    d3 = Day3(data)
    r = d3.get_results()
    assert r == [512794, 00], "Day 3 results are inaccurate."
