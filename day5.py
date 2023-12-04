class Day5:

    def __init__(self, data):
        self.data = data

    def day5_part1(self):
        with open(self.data) as fp:
            for line in fp:
                pass
        return True


if __name__ == '__main__':
    d5 = Day5('data/day5_input.txt')
    print(d5.day5_part1())