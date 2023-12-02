# This is the day 1 Advent of Code task as Python script.

def processSnowCalibration(cal):
    with open(cal) as fp:
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
                if line.find(nr) >= 0:
                    nr_dict[line.find(nr)] = str_numbers[nr]

            for i, value in enumerate(line):
                if is_int(value):
                    nr_dict[i] = int(value)
            print(nr_dict)
            print(int(str(nr_dict[min(nr_dict.keys())]) + str(nr_dict[max(nr_dict.keys())])))
            all_numbers.append(int(str(nr_dict[min(nr_dict.keys())]) + str(nr_dict[max(nr_dict.keys())])))
        print(all_numbers)
        print(sum(all_numbers))


def is_int(v):
    try:
        f = int(v)
        return True
    except:
        pass # return False


if __name__ == '__main__':
    processSnowCalibration('day1_test_input.txt')
