from random import randint


def guest_number(picked_number, n):
    if n == 0:
        print(picked_number)
        return
    quested_number = int(input('Введите число: '))
    if picked_number == quested_number:
        print('Число отгадано!!!')
        return
    if picked_number < quested_number:
        print('Загаданное число меньше')
    if picked_number > quested_number:
        print('Загаданное число больше')
    guest_number(picked_number, n - 1)


if __name__ == '__main__':
    guest_number(randint(0, 100), 10)

