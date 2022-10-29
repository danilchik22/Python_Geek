import random

import memory_profiler
import numpy


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        print(m2[0] - m1[0])
        return res
    return wrapper


@decor
def check_3_optimized(lst_obj):
    """Функция должная вернуть True, если все элементы списка различаются.
    Алгоритм 3:
    Вначале выполним для списка сортировку, далее, сравниваем элементы попарно
    Если присутствуют дубли, они будут находиться рядом.
    Сложность: O(n*log(n))
    """
    num_lst = numpy.array(lst_obj)
    for i in range(len(num_lst) - 1):
        if num_lst[i] == num_lst[i+1]:
            return False
    return True


@decor
def check_3(lst_obj):
    lst_copy = list(lst_obj)
    lst_copy.sort()
    print(lst_copy)
    for i in range(len(lst_obj) - 1):
        if lst_copy[i] == lst_copy[i+1]:
            return False
    return True


lst = [random.randint(0, 1000) for i in range(10000)]
print(check_3_optimized(lst))
print(check_3(lst))

# В оптимизированной функции с помощью numpy в сотни раз меньше расход памяти