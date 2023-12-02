import pytest
from day2 import Day2


@pytest.fixture
def setup():
    d2 = Day2('../data/day2_input.txt')
    games = d2.count_cubes()
    load = {'red': 12, 'green': 13, 'blue': 14}
    return d2, games, load


@pytest.fixture
def data():
    d2 = Day2('../data/day2_test_input.txt')
    cubes = [{'red': 4, 'green': 2, 'blue': 6},
             {'red': 1, 'green': 3, 'blue': 4},
             {'red': 20, 'green': 13, 'blue': 6},
             {'red': 14, 'green': 3, 'blue': 15},
             {'red': 6, 'green': 3, 'blue': 2}]
    return d2, cubes


def test_count_cubes(data):
    d2, results = data
    assert d2.count_cubes() == results, \
        "Day 1, part1: counting of cubes per game is inaccurate."


def test_possible_games(setup):
    d2, games, load = setup
    assert d2.possible_games(load, games) == 2720, \
        "Day 2, part1: Number or indexes of possible games is inaccurate."


def test_power_of_games(setup):
    d2, games, _ = setup
    assert d2.power_of_games(games) == 71535, \
        "Day 2, part2: Value of power of all games in unexpected."
