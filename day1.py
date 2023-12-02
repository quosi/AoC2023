# This is the day 1 Advent of Code task as Python script.

class Day1:

    def __init__(self, data):
        self.data = data

    def day1_part1(self):
        with open(self.data) as fp:
            all_numbers = []

            for line in fp:
                two_digit_nr = []
                for value in line:
                    if value.isdigit():
                        two_digit_nr.append(value)
                if len(two_digit_nr) > 0:
                    all_numbers.append(int(two_digit_nr[0] + two_digit_nr[-1]))
                else:
                    print('Input line contains no digits.')
            return sum(all_numbers)

    def day1_part2(self):
        with open(self.data) as fp:
            all_numbers = []
            str_numbers = {'one': 1,
                           'two': 2,
                           'three': 3,
                           'four': 4,
                           'five': 5,
                           'six': 6,
                           'seven': 7,
                           'eight': 8,
                           'nine': 9}

            for line in fp:
                nr_dict = {}

                for nr in list(str_numbers.keys()):

                    start_index = 0
                    while start_index < len(line):
                        j = line.find(nr, start_index)
                        if (j != -1):
                            nr_dict[j] = str_numbers[nr]
                            start_index = j + 1
                        else:
                            start_index += 1

                for i, value in enumerate(line):
                    if value.isdigit():
                        nr_dict[i] = int(value)

                all_numbers.append(int(str(nr_dict[min(nr_dict.keys())]) + str(nr_dict[max(nr_dict.keys())])))
            return sum(all_numbers)

    def get_results(self) -> [int, int]:
        return self.day1_part1(), self.day1_part2()

if __name__ == '__main__':
    data = 'data/day1_input.txt'
    d1 = Day1(data)
    print(f'Day1 task1: {d1.day1_part1()}')  # 55834
    print(f'Day1 task2: {d1.day1_part2()}')  # 53221