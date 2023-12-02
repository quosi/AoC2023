# This is the day 1 Advent of Code task as Python script.

class Day1:

    def __init__(self, data):
        self.data = data

    def day1_part1(self):
        with open(self.data) as fp:
            all_numbers = []

            for line in fp:
                two_digit_nr = []
                for i, value in enumerate(line):
                    if self.is_int(value):
                        two_digit_nr.append(int(value))
                if len(two_digit_nr) < 2:
                    two_digit_nr.append(two_digit_nr[0])
                if len(two_digit_nr) > 2:
                    two_digit_nr = [two_digit_nr[0], two_digit_nr[-1]]
                all_numbers.append(int(str(two_digit_nr[0]) + str(two_digit_nr[1])))

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
                    for i in range(len(line)):
                        j = line.find(nr, start_index)
                        if (j != -1):
                            nr_dict[j] = str_numbers[nr]
                            start_index = j + 1

                for i, value in enumerate(line):
                    if self.is_int(value):
                        nr_dict[i] = int(value)

                all_numbers.append(int(str(nr_dict[min(nr_dict.keys())]) + str(nr_dict[max(nr_dict.keys())])))
            return sum(all_numbers)

    def is_int(self, v) -> bool:
        try:
            f = int(v)
            return True
        except:
            return False
