from collections import deque


class Number16:
    numbers_dict = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'A': 10, 'B': 11,
                       'C': 12, 'D': 13, 'E': 14, 'F': 15}
    numbers_dict = numbers_dict | {value: key for key, value in numbers_dict.items()}

    def __init__(self, number):
        self.figures = deque(number)

    def __add__(self, other):
        result = deque()
        oth = deque(other.figures)
        sel = deque(self.figures)
        adding = 0
        if len(sel) > len(oth):
            for i in range(len(oth)):
                sum_numbers = Number16.numbers_dict[oth.pop()] + Number16.numbers_dict[sel.pop()] + \
                              adding
                if sum_numbers > 15:
                    adding = 1
                    added_figures = sum_numbers - 16
                    result.appendleft(Number16.numbers_dict[added_figures])
                else:
                    adding = 0
                    result.appendleft(Number16.numbers_dict[sum_numbers])
            for i in range(len(sel)):
                sum_numbers = Number16.numbers_dict[sel.pop()] + adding
                if sum_numbers > 15:
                    adding = 1
                    added_figures = sum_numbers - 16
                    result.appendleft(self.numbers_dict[added_figures])
                else:
                    adding = 0
                    result.appendleft(self.numbers_dict[sum_numbers])
            if adding == 1:
                result.appendleft(self.values_dict_pop[1])
        else:
            for i in range(0, len(sel)):
                sum_numbers = Number16.numbers_dict[sel.pop()] + Number16.numbers_dict[oth.pop()] + \
                              adding
                if sum_numbers > 15:
                    adding = 1
                    added_figures = sum_numbers - 16
                    result.appendleft(Number16.numbers_dict[added_figures])
                else:
                    adding = 0
                    result.appendleft(Number16.numbers_dict[sum_numbers])
            for i in range(len(oth)):
                sum_numbers = Number16.numbers_dict[oth.pop()] + adding
                if sum_numbers > 15:
                    adding = 1
                    added_figures = sum_numbers - 16
                    result.appendleft(other.values_dict_pop[added_figures])
                else:
                    adding = 0
                    result.appendleft(other.values_dict_pop[sum_numbers])
            if adding == 1:
                result.appendleft(other.values_dict_pop[1])
        return Number16(result)

    def __mul__(self, other):
        HEX_NUM = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
                   'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15,
                   0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9',
                   10: 'A', 11: 'B', 12: 'C', 13: 'D', 14: 'E', 15: 'F'}
        result = deque()
        spam = deque([deque() for _ in range(len(other.figures))])

        x, y = self.figures.copy(), deque(other.figures)

        for i in range(len(y)):
            m = Number16.numbers_dict[y.pop()]

            for j in range(len(x) - 1, -1, -1):
                spam[i].appendleft(m * Number16.numbers_dict[x[j]])

            for _ in range(i):
                spam[i].append(0)

        transfer = 0

        for _ in range(len(spam[-1])):
            res = transfer

            for i in range(len(spam)):
                if spam[i]:
                    res += spam[i].pop()

            if res < 16:
                result.appendleft(Number16.numbers_dict[res])

            else:
                result.appendleft(Number16.numbers_dict[res % 16])
                transfer = res // 16

        if transfer:
            result.appendleft(Number16.numbers_dict[transfer])

        return Number16(result)


num2 = Number16('A2')
num1 = Number16('C4F')
print((num1 + num2).figures)
print((num1*num2).figures)
print(num2.figures)
