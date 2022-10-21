import timeit


def time_of_work(func):
    def wrapper(*args, **kwargs):
        print(
            f'Время выполнения функции {func.__name__}: {timeit.timeit(func.__name__, number=100000, globals=globals())}')
        return func(*args, **kwargs)

    return wrapper


def revers(enter_num, revers_num=0):
    if enter_num == 0:
        return
    else:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
        revers(enter_num, revers_num)


@time_of_work
def revers_2(enter_num, revers_num=0):
    while enter_num != 0:
        num = enter_num % 10
        revers_num = (revers_num + num / 10) * 10
        enter_num //= 10
    return int(revers_num)


@time_of_work
def revers_3(enter_num):
    enter_num = str(enter_num)
    revers_num = enter_num[::-1]
    return revers_num


@time_of_work
def revers_4(enter_num):
    num_str = str(enter_num)
    num_str = ''.join(reversed(num_str))
    num = int(num_str)
    return num


print(f'Время выполнения функции reverse: {timeit.timeit("revers", number=100000, globals=globals())}')
# Функция reverse - рекурсивная, поэтому при применении декоратора время выполнения будет выводиться каждый раз,
# поэтому необходимо выводить время выполнения без декоратора
print(revers(345689))
print(revers_2(345689))
print(revers_3(345689))
print(revers_4(345689))

# Наиболее эффективна реализация revers_4, потому что к числу не нужно применять вычислительные операции, в случае
# большого числа алгоритм будет отрабатывать одинаково эффективно
