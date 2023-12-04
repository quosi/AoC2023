import re


class Day4:

    def __init__(self, data):
        self.data = data

    def calc_win_cards(self):
        with open(self.data) as fp:
            win_nums = []
            card_nums = []
            pattern = re.compile(r"Card\s+\d+:\s*(.*)\s\|\s(.*)")
            for line in fp:
                match = re.search(pattern, line)
                win_nums.append([int(n) for n in match.group(1).split()])
                card_nums.append([int(n) for n in match.group(2).split()])

        resulting_n = []
        for i in range(len(card_nums)):
            card_res = []
            for n in card_nums[i]:
                if n in win_nums[i]:
                    card_res.append(n)
            resulting_n.append(len(card_res))
        return resulting_n


    def day4_part1(self):
        calc = [n for n in self.calc_win_cards() if n > 0]
        result = [2**(n-1) for n in calc]
        return sum(result)

    def day4_part2(self):
        resulting_wins = self.calc_win_cards()
        num_cards = [1] * len(resulting_wins)
        print(num_cards)
        print(len(num_cards))
        print(resulting_wins)
        print(len(resulting_wins))
        for i, n in enumerate(resulting_wins):
            j = i+1
            while n > 0:
                num_cards[j] += 1
                n -= 1
                j += 1
        return num_cards

    def get_results(self) -> [int, int]:
        return [self.day4_part1(), self.day4_part2()]

if __name__ == '__main__':
    data_ = 'data/day4_input.txt'
    d4 = Day4(data_)
    wins = d4.calc_win_cards()
    r = d4.day4_part1(wins)
    # assert r == 13 # test result || real result r = 18653
    w = d4.day4_part2(wins)
    print(w)
    print(sum(w))  # r = 1030 to low
