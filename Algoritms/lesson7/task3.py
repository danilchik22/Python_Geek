import timeit
import random
import statistics


m = 10
array = [random.randint(0, 100) for i in range(2 * m + 1)]
print(array)
print(f'Медиана: {statistics.median(array)}')
print(timeit.timeit('statistics.median(array)', globals=globals(), number=10))
print('-----------------------------------')
m = 100
array = [random.randint(0, 100) for i in range(2 * m + 1)]
print(array)
print(f'Медиана: {statistics.median(array)}')
print(timeit.timeit('statistics.median(array)', globals=globals(), number=10))
print('-----------------------------------')
m = 1000
array = [random.randint(0, 100) for i in range(2 * m + 1)]
print(array)
print(f'Медиана: {statistics.median(array)}')
print(timeit.timeit('statistics.median(array)', globals=globals(), number=10))

# самый быстрый способ - с помощью встроенной функции, импортированной из библиотеки statistics