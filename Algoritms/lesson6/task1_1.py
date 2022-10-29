import random

import memory_profiler
from memory_profiler import profile

"""
Представлен список чисел. Необходимо вывести те его элементы, значения которых больше предыдущего, например:
src = [300, 2, 12, 44, 1, 1, 4, 10, 7, 1, 78, 123, 55]
result = [12, 44, 4, 10, 78, 123]
"""


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        func(args[0])
        m2 = memory_profiler.memory_usage()
        print(m2[0] - m1[0])
    return wrapper


@decor
def view_result(src):
    result = [src[index] for index in range(1, len(src)) if src[index] > src[index - 1]]
    print(result)


@decor
def view_result_optimize(src):
    result = (src[index] for index in range(1, len(src)) if src[index] > src[index - 1])
    for i in result:
        print(i)


arr = [random.randint(0, 100) for i in range(1000)]
view_result(arr)
view_result_optimize(arr)

# вместо массива используем генератора, чтобы не загружать память, так мы можем вывести хоть миллиард чисел без потери
# памяти
