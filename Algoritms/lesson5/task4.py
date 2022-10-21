import random
import time
import timeit
from collections import OrderedDict
usual_dict = {}
ord_dict = OrderedDict()
time1 = time.time()
for i in range(1000000, 0, -1):
    usual_dict[i] = i
time2 = time.time()
print(f'Время добавления 1000000 элементов в обычный словарь: {time2-time1}')
time1 = time.time()
for i in range(1000000, 0, -1):
    ord_dict[i] = i
time2 = time.time()
print(f'Время добавления 100000 элементов в OrderedDict: {time2-time1}')

print(f'Время получения элемента по ключу в dict: '
      f'{timeit.timeit(stmt="usual_dict.get(900)", number = 1000000, globals=globals())}')
print(f'Время получения элемента по ключу в OrderedDict: '
      f'{timeit.timeit(stmt="ord_dict.get(900)", number = 1000000, globals=globals())}')


print(f'Время удаления элемента по ключу в dict: '
      f'{timeit.timeit(stmt="usual_dict.pop(900)", number = 1, globals=globals())}')
print(f'Время удаления элемента по ключу в OrderedDict: '
      f'{timeit.timeit(stmt="ord_dict.pop(900)", number = 1, globals=globals())}')

# Добавление элементов, получение и удаление в обычный словарь и упорядоченный словарь происходит примерно одинаково
# по времени. Мы используем Python версии 3.10, в которой словарь по умолчанию упорядочен.
# До версии 3.6 OrderedDict имеет смысл использовать, если важен порядок пар ключ-значение в словаре. Начиная от версии
# 3.6 смысла использовать OrderedDict не вижу, т.к. необходимые функции имеются по умолчанию. Имеет смысл использовать
# OrderedDict, если нам необходима совместимость версий.




