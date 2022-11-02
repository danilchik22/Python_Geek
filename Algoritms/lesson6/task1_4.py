"""
Задание 3.
Для этой задачи
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
3) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Имеется хранилище с информацией о компаниях: название и годовая прибыль.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, реализовать словарь.
Реализуйте поиск трех компаний с наибольшей годовой прибылью.
Выведите результат.
Примечание: ПРОШУ ВАС ВНИМАТЕЛЬНО ЧИТАТЬ ЗАДАНИЕ!
"""
import memory_profiler


def decor(func):
    def wrapper(*args, **kwargs):
        m1 = memory_profiler.memory_usage()
        res = func(args[0])
        m2 = memory_profiler.memory_usage()
        print(m2[0] - m1[0])
        return res

    return wrapper


@decor
def search_company_2(dictt):
    if len(dictt) < 3:  # O(1)
        return None
    lst = list(dictt.values())  # O(n)
    max = [lst.pop(), lst.pop(), lst.pop()]  # O(1)
    max.sort(reverse=True)  # O(1) - сортировка всего 3х элементов при любых n, поэтому O - константа.
    for i in lst:  # O(n)
        for j in range(0, 3):  # O(1) - цикл по 3м элементам всегда
            if i > max[j]:  # O(1)
                max[j] = i  # O(1)
                break
    result = {}
    for key, value in dictt.items():  # O(n)
        for j in range(0, 3):  # O(1)
            if value == max[j]:  # O(1)
                result[key] = value  # O(1)
    return result


# оптимизированный по памяти алгоритм:

@decor
def search_company_opt(dictt):
    if len(dictt) < 3:  # O(1)
        return None
    lst = list(dictt.values())  # O(n)
    max = [lst.pop(), lst.pop(), lst.pop()]  # O(1)
    max.sort(reverse=True)  # O(1) - сортировка всего 3х элементов при любых n, поэтому O - константа.
    for i in lst:  # O(n)
        for j in range(0, 3):  # O(1) - цикл по 3м элементам всегда
            if i > max[j]:  # O(1)
                max[j] = i  # O(1)
                break
    del lst
    result = {}
    for key, value in dictt.items():  # O(n)
        for j in range(0, 3):  # O(1)
            if value == max[j]:  # O(1)
                result[key] = value  # O(1)
    return result


dict2 = search_company_2({'com1': 345, 'comm': 10, 'com2': 456, 'com3': 9856, 'com4': 23, 'com5': 2332435})
dict1 = search_company_opt({'com1': 345, 'comm': 10, 'com2': 456, 'com3': 9856, 'com4': 23, 'com5': 2332435})
print("Компании с наибольшей прибылью: ")
for key, value in dict2.items():
    print(f'Компания {key}. Прибыль: {value}')
for key, value in dict1.items():
    print(f'Компания {key}. Прибыль: {value}')

# Так как копия массива больше не нужна, удалили её через del, освободив таким образом память