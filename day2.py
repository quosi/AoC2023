import re


class Day2:
    def __init__(self, data):
        self.data = data

    def count_cubes(self):
        with open(self.data) as fp:
            games = []
            pattern_red = r'(\d*) red'
            pattern_green = r'(\d*) green'
            pattern_blue = r'(\d*) blue'

            for line in fp:
                count = {
                    'red': max([int(n) for n in re.findall(pattern_red, line)]),
                    'green': max([int(n) for n in re.findall(pattern_green, line)]),
                    'blue': max([int(n) for n in re.findall(pattern_blue, line)])
                }
                games.append(count)
        return games

    def possible_games(self, load, games) -> int:
        ''' Day2 Task 1 '''
        possible_g = []

        for i, game in enumerate(games):
            if game['red'] <= load['red'] and game['green'] <= load['green'] and game['blue'] <= load['blue']:
                possible_g.append(i + 1)
        return sum(possible_g)

    def power_of_games(self, games) -> int:
        ''' Day2 Task 2'''
        return sum([game['red'] * game['green'] * game['blue'] for game in games])

    def get_results(self) -> [int, int]:
        ref = {'red': 12, 'green': 13, 'blue': 14}
        cubes = self.count_cubes()
        return self.possible_games(ref, cubes), self.power_of_games(cubes)


if __name__ == '__main__':
    load_ = {'red': 12, 'green': 13, 'blue': 14}
    data_ = 'data/day2_test_input.txt'
    d2 = Day2(data_)
    games_ = d2.count_cubes()
    print(games_)
    print(f'Sum of possible games indexes: {d2.possible_games(load_, games_)}')  # 2720
    print(f'Sum of power of each game: {d2.power_of_games(games_)}')  # 71535
