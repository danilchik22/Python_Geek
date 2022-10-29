import time
import timeit
from collections import deque

arr_deq = deque()
arr_lst = []

exp1 = """for i in range(10000):
    arr_deq.append(34)
"""
print(f'Время добавления элемента в deque методом append: {timeit.timeit(stmt=exp1, number = 1000, globals=globals())}')

exp2 = """for i in range(10000):
    arr_lst.append(34)"""
print(f'Время добавления в list методом append: {timeit.timeit(stmt=exp2, number = 1000, globals=globals())}')

exp3 = """for i in range(10000):
    arr_deq.pop()"""
print(f'Время взятия последнего элемента в deque: '
      f'{timeit.timeit(stmt=exp3, number = 1000, globals=globals())}')

exp4 = """
for i in range(10000):
    arr_lst.pop()
    """
print(f'Время взятия последнего элемента в list: '
      f'{timeit.timeit(stmt=exp4, number = 1000, globals=globals())}')

arr2 = [i for i in range(1000)]

exp5 = """arr_deq.extend(arr2)"""
print(f'Время расширения deque с помощью extend: '
      f'{timeit.timeit(stmt=exp5, number = 1000, globals=globals())}')

exp6 = """arr_lst.extend(arr2)"""
print(f'Время расширения list с помощью extend: '
      f'{timeit.timeit(stmt=exp6, number = 1000, globals=globals())}')

#Время добавления с помощью append, взятие элемента с конца с помощью pop, расширение с помощью extend в deque и list
# примерно одинаковое, список работает немного быстрее.

exp7 = """
for i in range(100):
    arr_deq.appendleft(55)
    """
print(f'Время добавления элемента в начало в deque: {timeit.timeit(stmt=exp7, number = 100, globals=globals())}')

exp8 = """
for i in range(100):
    arr_lst.insert(0, 55)
    """
print(f'Время добавления элемента в начало в list: {timeit.timeit(stmt=exp8, number = 100, globals=globals())}')

exp9 = """
for i in range(100):
    arr_deq.popleft()
    """
print(f'Время взятия элемента из начала deque: {timeit.timeit(stmt=exp9, number = 100, globals=globals())}')

exp10 = """
for i in range(100):
    arr_lst.pop(0)
    """
print(f'Время взятия элемента из начала list: {timeit.timeit(stmt=exp10, number = 100, globals=globals())}')

exp11 = """arr_deq.extendleft(arr2)"""
print(f'Время расширения deque слева: {timeit.timeit(stmt=exp11, number = 1000, globals=globals())}')

exp12 = """
arr2 + arr_lst
"""
print(f'Время расширения list слева: {timeit.timeit(stmt=exp12, number = 1000, globals=globals())}')

# Получение и добавление элементов в начало в deque происходит очень быстро по сравнению с list, разница колоссальна,
# Расширение списка слева тоже происходит достаточно долго в отличие от расширения deque слева.

exp13 = """
arr_deq[800]
"""
print(f'Время получения элемента в deque: {timeit.timeit(stmt=exp13, number = 1000, globals=globals())}')

exp14 = """
arr_lst[800]
"""
print(f'Время получения элемента в deque: {timeit.timeit(stmt=exp13, number = 1000, globals=globals())}')

# Получение элемента по произвольному индексу происходит одинаково по времени


