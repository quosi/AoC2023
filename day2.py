import re


def count_cubes(data):
    with open(data) as fp:
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


def possible_games(load, games):
    possible_g = []

    for i, game in enumerate(games):
        if game['red'] <= load['red'] and game['green'] <= load['green'] and game['blue'] <= load['blue']:
            possible_g.append(i + 1)
    return possible_g


def power_of_games(games):
    return sum([game['red'] * game['green'] * game['blue'] for game in games])


if __name__ == '__main__':
    load_ = {'red': 12, 'green': 13, 'blue': 14}
    data_ = 'data/day2_input.txt'
    games_ = count_cubes(data_)
    result = possible_games(load_, games_)
    print(f'Sum of possible games indexes: {sum(result)}')  # 2720
    print(f'Sum of power of each game: {power_of_games((games_))}')  # 71535
