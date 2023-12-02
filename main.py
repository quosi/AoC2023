
import pandas as pd
from day1 import Day1

def show_results(d1):

    data = [[1, 1, d1.day1_part1()], [1, 2, d1.day1_part2()]]
    df = pd.DataFrame(data, columns=['Day', 'Part', 'Result'])
    print(df)

if __name__ == '__main__':
    d1 = Day1('data/day1_input.txt')
    assert d1.day1_part1() == 55834, "Day 1, part1 shows unexpected results."
    assert d1.day1_part2() == 53221, "Day 1, part2 shows unexpected results."
    show_results(d1)
