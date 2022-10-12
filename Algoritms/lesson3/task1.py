import random
import time


def time_function(func):
    def wrapper(*args, **kwargs):
        time_list_fill_one = round(time.perf_counter() * 1000)
        result_funct = func(*args, **kwargs)
        time_list_fill_two = round(time.perf_counter() * 1000)
        print(f'Время выполнения функции {func.__name__}: {time_list_fill_two - time_list_fill_one}')
        return result_funct

    return wrapper


# Задание а)
@time_function
def fill_list():
    our_list = []
    for i in range(0, 1000000):
        our_list.append(i)  # O(1)
    return our_list


@time_function
def fill_dict():
    dict_one = {}
    for i in range(0, 1000000):
        dict_one[i] = i  # O(1)
    return dict_one


# При использовании функции append для списка, временная сложность - константа, потому что во внутренней структуре
# не будут перемещаться элементы, вставка происходит в конец. Если используем insert, то временная сложность O(n),
# потому что мы не знаем заранее куда вставляем элемент. В словаре при вставке вычисляется хэш ключа, соответственно,
# при заполнении словаря и списка с конца заполнение списка будет немного быстрее.

# Задание б)

@time_function
def get_from_list(one_list):
    for i in range(0, 1000000):
        element = one_list[i]  # O(1)


@time_function
def get_from_dict(one_dict):
    for i in range(0, 1000000):
        element = one_dict[i]  # O(1)


# Время получения элемента из словаря и списка примерно одинаково. В списке доступ к элементу происходит
# по известному адресу в ячейке памяти. В словаре по известному хешу.

# Задание в)

@time_function
def delete_from_list_10000(one_list):
    for i in range(0, 10000):
        one_list.remove(i)  # O(n)


@time_function
def delete_from_dict_1mil(one_dict):
    for i in range(0, 1000000):
        one_dict.pop(i)  # O(1)


# Если удалять элемент из списка с начала, то эта операция будет происходить очень долго, потому что нужно будет
# переставить все элементы. В словаре же пары ключ-значение между собой не связаны, поэтому это не требуется,
# соответственно удаление происходит намного быстрее.

if __name__ == '__main__':
    our_list1 = fill_list()
    our_dict1 = fill_dict()
    get_from_list(our_list1)
    get_from_dict(our_dict1)
    delete_from_list_10000(our_list1)
    delete_from_dict_1mil(our_dict1)
