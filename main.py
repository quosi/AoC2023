import pandas as pd
from day1 import Day1
from day2 import Day2
from day3 import Day3
from day4 import Day4

def show_results(data):
    df_data = []
    for i, d in enumerate(data):
        r1, r2 = d.get_results()
        df_data.append([i + 1, 1, r1])
        df_data.append([i + 1, 2, r2])

    df = pd.DataFrame(df_data, columns=['Day', 'Part', 'Result'])
    print(df)


if __name__ == '__main__':
    d1 = Day1('data/day1_input.txt')
    d2 = Day2('data/day2_input.txt')
    d3 = Day3('data/day3_input.txt')
    d4 = Day4('data/day4_input.txt')
    games = d2.count_cubes()
    load = {'red': 12, 'green': 13, 'blue': 14}
    data = [d1, d2, d3, d4]

    assert d1.day1_part1() == 55834, "Day 1, part1 shows unexpected results."
    assert d1.day1_part2() == 53221, "Day 1, part2 shows unexpected results."
    assert d2.possible_games(load, games) == 2720, "Day 2, part1 shows unexpected results."
    assert d2.power_of_games(games) == 71535, "Day 2, part2 shows unexpected results."

    show_results(data)
