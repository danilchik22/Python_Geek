import timeit
from collections import Counter


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
    return f'Чаще всего встречается число  {max(Counter(array), key=Counter(array).get)}' \
           f' Оно появилось в массиве {array.count(max(Counter(array), key=Counter(array).get))} раз(а)'


array = [1, 3, 1, 3, 4, 5, 1]
print(func_1(array))
print(func_2(array))
print(func_3(array))

# Встроенная функция Counter ищет число вхождений у каждого элемента, она работает быстрее, а потом уже
# берем максимальное число вхождений из полученного словаря в результате функции Counter