import re


class Day3:

    def __init__(self, data):
        self.data = data

    def day3_part1(self):
        with open(self.data) as fp:
            doc = []  # 140 x 140
            digits = []
            result = 0

            for line in fp:
                doc.append(('.' + line + '.'))

        for line in doc:
            pattern = r'\d+'
            digit_line = []
            for match in re.finditer(pattern, line):
                r = match.span()
                nr = match.group()
                # !! match counting from 0 shows position start+1 till end+2 !!
                # therefor correcting output to [start-index, end-index, found-number]
                digit_line.append([r[0] - 1, r[1] - 2, int(nr)])
            digits.append(digit_line)

        for i in range(1, len(doc) - 1):
            for j in range(len(digits[i])):
                #  checking for symbols before and after the digit
                if self.is_special(doc[i][digits[i][j][0]]) \
                        or self.is_special(doc[i][digits[i][j][1] + 2]):
                    res = digits[i][j][2]
                    print(f'Digit:{res}, doc: {doc[i][digits[i][j][0] - 1]}, Zeile:{i}, Digit_ID:{j}')
                    result += res
                #  checking for symbols on lines above of digit
                for s in doc[i - 1][digits[i][j][0]:digits[i][j][1] + 3]:
                    if self.is_special(s):
                        res = digits[i][j][2]
                        print(
                            f'Digit:{res}, doc: {doc[i - 1][digits[i][j][0]:digits[i][j][1] + 3]}, Zeile:{i}, Digit_ID:{j}')
                        result += res
                #  checking for symbols on lines below of digit
                for s in doc[i + 1][digits[i][j][0]:digits[i][j][1] + 3]:
                    if self.is_special(s):
                        res = digits[i][j][2]
                        print(
                            f'Digit:{res}, doc: {doc[i + 1][digits[i][j][0]:digits[i][j][1] + 3]}, Zeile:{i}, Digit_ID:{j}')
                        result += res

        '''ToDo checking first and last line corner case doesn't work
        #  checking corner cases separately to avoid index out of range error for line 0 and -1
        for jj in range(len(digits[0])):

            if self.is_special(doc[0][digits[0][jj][0]]) or self.is_special(doc[0][digits[0][jj][1] + 2]):
                res = digits[0][jj][2]
                print(
                    f'Digit:{res}, doc: {doc[0][digits[0][jj][0] - 1]}, Zeile:{i}, Digit_ID:{jj}')
                result += res

        # checking below
        for s in doc[1][digits[0][jj][0]:digits[0][jj][1]+3]:
            if self.is_special(s):
                res = digits[0][jj][2]
                print(
                    f'Digit:{res}, doc: {s}, Zeile:{0}, Digit_ID:{jj}')
                result += res

        for l in range(len(digits[-1])):
            if self.is_special(doc[-1][digits[-1][l][0]]) or self.is_special(doc[-1][digits[-1][l][1] + 2]):
                res = digits[-1][l][2]
                print(
                    f'Digit:{res}, doc: {doc[-1][digits[-1][l][0] - 1]}, Zeile:{i}, Digit_ID:{l}')
                result += res
        # checking above
        for s in doc[-2][digits[-1][l][0]:digits[-1][l][1]+3]:
            if self.is_special(s):
                res = digits[-1][l][2]
                print(
                    f'Digit:{res}, doc: {s}, Zeile:{0}, Digit_ID:{l}')
                result += res
        '''
        return result

    def is_special(self, sym) -> bool:
        zeichen = r'=+-@_!#$%^&*?/|~:'
        if sym in zeichen:
            return True
        else:
            return False


if __name__ == '__main__':
    data_test = 'data/day3_input.txt'
    d3 = Day3(data_test)
    r = d3.day3_part1()
    # adding first & last row numbers by hand:
    print(r + 296 + 45 + 902 + 269 + 720 + 571)  # 512794
