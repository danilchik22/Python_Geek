from collections import deque, Counter


class Tree:
    def __init__(self, left_child, right_child, weight):
        self.left_child = left_child
        self.right_child = right_child
        self.weight = weight


def haffman(lst):
    if len(lst) == 0:
        return 0
    frequency = deque(sorted(Counter(lst).items(), key=lambda item: item[1]))
    while len(frequency) > 1:
        weight = frequency[0][1] + frequency[1][1]
        if len(frequency) == 2:
            frequency.append((Tree(frequency.popleft()[0], frequency.popleft()[0], weight), weight))
        for i in range(2, len(frequency)):
            if frequency[i][1] >= weight:
                frequency.insert(i - 2, (Tree(frequency.popleft()[0], frequency.popleft()[0], weight), weight))
                break
            if i == (len(frequency) - 1):
                frequency.append((Tree(frequency.popleft()[0], frequency.popleft()[0], weight), weight))
    return frequency[0][0]


dict_chars = {}


def do_table_code(tree, path=''):
    if not isinstance(tree, Tree):
        dict_chars[tree] = path
    else:
        do_table_code(tree.left_child, f'{path}0')
        do_table_code(tree.right_child, f'{path}1')


def do_code(table, txt):
    result = ''
    for i in txt:
        result = f'{result}{table[i]} ' # для наглядности сделал пробел, в итоговом коде его нужно убрать
    return result


text1 = 'привет пипеткам пипеточным'
do_table_code(haffman(text1))
print(dict_chars)
print(do_code(dict_chars, text1))

