import random
import timeit


def sort_bubble(lst):
    lst_copy = lst[:]
    for j in range(len(lst_copy)):
        for i in range(len(lst_copy) - 1):
            if lst_copy[i] < lst_copy[i + 1]:
                tmp = lst_copy[i]
                lst_copy[i] = lst_copy[i + 1]
                lst_copy[i + 1] = tmp
    return lst_copy


def sort_bubble_opt(lst):
    lst_copy = lst[:]
    changed = False
    for j in range(len(lst_copy)):
        if not changed and j != 0:
            break
        changed = False
        for i in range(len(lst_copy) - 1):
            if lst_copy[i] < lst_copy[i + 1]:
                tmp = lst_copy[i]
                lst_copy[i] = lst_copy[i + 1]
                lst_copy[i + 1] = tmp
                changed = True
    return lst_copy


arr = [random.randint(-100, 100) for i in range(50)]
print(sort_bubble(arr))
print(timeit.timeit('sort_bubble_opt(arr)', globals=globals(), number=10000))
print(timeit.timeit('sort_bubble(arr)', globals=globals(), number=10000))
