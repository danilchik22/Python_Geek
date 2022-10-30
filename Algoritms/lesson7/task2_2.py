import timeit
import random


def median(lst):
    lst_cp = lst[:]
    for i in range(len(lst)//2):
        lst_cp.remove(max(lst_cp))
        lst_cp.remove(min(lst_cp))
    return lst_cp[0]


m = 10
array = [random.randint(0, 100) for i in range(2*m+1)]
print(array)
print(f'Медиана: {median(array)}')
print(timeit.timeit('median(array)', globals=globals(), number=10))
print('-----------------------------------')
m = 100
array = [random.randint(0, 100) for i in range(2*m+1)]
print(array)
print(f'Медиана: {median(array)}')
print(timeit.timeit('median(array)', globals=globals(), number=10))
print('-----------------------------------')
m = 1000
array = [random.randint(0, 100) for i in range(2*m+1)]
print(array)
print(f'Медиана: {median(array)}')
print(timeit.timeit('median(array)', globals=globals(), number=10))


# в разы быстрее чем сортировкой