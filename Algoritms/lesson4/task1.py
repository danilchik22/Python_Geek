from timeit import timeit


def func_1(nums):
    new_arr = []
    for i in range(len(nums)):
        if nums[i] % 2 == 0:
            new_arr.append(i)
    return new_arr


def func_2(nums):
    new_arr = [i for i in nums if i % 2 == 0]
    return new_arr


print(timeit("func_1", number=10000000, globals=globals()))
print(timeit("func_2", number=10000000, globals=globals()))
# Был создан массив с помощью list_comprehention. Создание массива с его помощью всегда производится быстрее, чем
# просто через цикл
