from random import randint


def check_statement(n):
    if n == 1:
        return 1
    return n + check_statement(n-1)


def calculate_right_statement(n):
    return n * (n+1)/2


if __name__ == '__main__':
# Проверим утверждение на 10 различных числах
    for i in range(0, 10):
        number = randint(0, 100)
        print(check_statement(number) == calculate_right_statement(number))