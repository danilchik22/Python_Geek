"""Подумайте, как можно сделать оптимизацию кода по памяти, по скорости.
Представлен список чисел. Определить элементы списка, не имеющие повторений. Сформировать из этих элементов список с сохранением порядка их следования в исходном списке, например:
src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
result = [23, 1, 3, 10, 4, 11]"""
import random

import memory_profiler


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        func(args[0])
        m2 = memory_profiler.memory_usage()
        print(m2[0] - m1[0])
    return wrapper

@decor
def view_result(src):
    tmp = set()
    result = []
    for number in src:
        if number not in tmp:
            tmp.add(number)
        else:
            tmp.remove(number)
    for number in src:
        if number in tmp:
            result.append(number)
    print(result)


@decor
def view_result2(src):
    result = []
    for number in src:
        if src.count(number) == 1:
            result.append(number)
    print(result)
# не создаем временного множества tmp, поэтому экономим память, но скорость страдает

srcc = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
view_result(srcc)
view_result2(srcc)
