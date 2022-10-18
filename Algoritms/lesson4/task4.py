import timeit


def time_of_work(func):
    def wrapper(*args, **kwargs):
        print(
            f'Время выполнения функции {func.__name__}: {timeit.timeit(func.__name__, number=100000, globals=globals())}')
        return func(*args, **kwargs)

    return wrapper


@time_of_work
def func_1(array):
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


@time_of_work
def func_2(array):
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


@time_of_work
def func_3(array):
    numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    counts = []
    for j in numbers:
        counts.append([array.count(j)])
    return f' Чаще всего встречается число {counts.index(max(counts))}, ' \
           f'оно появилось в массиве {max(counts)} раза'


array = [1, 3, 1, 3, 4, 5, 1]
print(func_1(array))
print(func_2(array))
print(func_3(array))

# Решение в func3 будет эффективнее на большом массиве, потому что не нужно будет пробегать по всему массиву чисел,
# вычисляя для каждого числа количество вхождений. Цифр всего 10 и достаточно для каждой цифры вычислить вхождение.