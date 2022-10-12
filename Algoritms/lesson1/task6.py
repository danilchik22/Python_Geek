class DeskBoard:
    def __init__(self):
        self.base = []
        self.reworking = []
        self.solved = []

    def __str__(self):
        return f'Список задач:\n {self.base}\n\n Список задач на доработку: \n {self.reworking}\n\n ' \
               f'Список решенных задач: \n {self.solved}'

    def add(self, task):
        self.base.append(task)

    def solve(self):
        if self.base:
            task = self.base[0]
            self.solved.append(task)
            self.base = self.base[1:]
            print(f'Задача {task} решена')
        else:
            print('Решать нечего')

    def send_rework(self):
        if self.solved:
            task = self.solved[0]
            self.reworking.append(task)
            self.solved = self.solved[1:]
            print(f'Задача {task} отправлена на доработку')
        else:
            print('Отправлять на переработку нечего')

    def rework(self):
        if self.reworking:
            task = self.reworking[0]
            self.solved.append(task)
            self.reworking = self.reworking[1:]
            print(f'Задача {task} доработана')
        else:
            print('Перерабатывать нечего')

board = DeskBoard()
board.add('Задача 1')
board.add('Задача 2')
board.add('Задача 3')
board.rework()
board.send_rework()
board.rework()
board.solve()
board.solve()
board.send_rework()
board.rework()
print(board)
