# This is the day 1 Advent of Code task as Python script.

def processSnowCalibration(cal):
    with open(cal) as fp:
        all_numbers = []
        str_numbers = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        for line in fp:
            two_digit_nr = []
            string_nr_dict = {}
            int_nr_dict = {}
            for nr in str_numbers:
                if line.find(nr) >= 0:
                    string_nr_dict[line.find(nr)] = nr
                    # print(f'{nr} at ', line.find(nr))
            print(string_nr_dict)

            for i, value in enumerate(line):
                if is_int(value):
                    two_digit_nr.append(int(value))
                    int_nr_dict[i] = int(value)
            if len(two_digit_nr) < 2:
                two_digit_nr.append(two_digit_nr[0])
            if len(two_digit_nr) > 2:
                two_digit_nr = [two_digit_nr[0], two_digit_nr[-1]]
            print(int_nr_dict)
            all_numbers.append(int(str(two_digit_nr[0]) + str(two_digit_nr[1])))
        print(sum(all_numbers))


def is_int(v):
    try:
        f = int(v)
        return True
    except:
        pass # return False


if __name__ == '__main__':
    processSnowCalibration('day1_input.txt')
