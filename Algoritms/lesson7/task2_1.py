import random
import timeit


def gnome_sort(lst):
    lst_c = lst[:]
    if len(lst_c) == 1:
        return lst_c
    for i in range(1, len(lst_c)):
        if lst_c[i] < lst_c[i - 1]:
            tmp = lst_c[i]
            lst_c[i] = lst_c[i - 1]
            lst_c[i - 1] = tmp
            for j in range(i, 0, -1):
                if lst_c[j] < lst_c[j - 1]:
                    tmp = lst_c[j]
                    lst_c[j] = lst_c[j - 1]
                    lst_c[j - 1] = tmp
    return lst_c


def median(lst):
    lst_sort = gnome_sort(lst)
    return lst_sort[int((len(lst_sort)-1)/2)]

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