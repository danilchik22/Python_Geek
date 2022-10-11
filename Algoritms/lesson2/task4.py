def sum(n):
    sum = 0
    for i in range(0, n):
        sum += (-0.5)**i
    return sum


def sum_of_row(n):
    if n == 1:
        return 1
    return (-0.5)**(n-1) + sum_of_row(n-1)


if __name__ == '__main__':
    print(sum_of_row(int(input('Введите количество элементов: '))))
