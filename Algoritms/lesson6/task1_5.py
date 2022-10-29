"""Задание 4.
Для этой задачи:
1) придумайте 2-3 решения (обязательно с различной сложностью)
2) оцените сложность каждого выражения в этих решениях в нотации О-большое
3) оцените итоговую сложность каждого решения в нотации О-большое
4) сделайте вывод, какое решение эффективнее и почему
Сама задача:
Пользователи веб-ресурса проходят аутентификацию.
В системе хранятся логин, пароль и отметка об активации учетной записи.
Нужно реализовать проверку, может ли пользователь быть допущен к ресурсу.
При этом его учетка должна быть активирована.
А если нет, то польз-лю нужно предложить ее пройти.
Приложение должно давать ответы на эти вопросы
 и быть реализовано в виде функции.
Для реализации хранилища можно применить любой подход,
который вы придумаете, например, применить словарь.
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
def check(listt):
    mas_false = []
    mas_true = []
    listt.sort() # O(n*log(n))
    fst = 0
    lst = len(listt) - 1 # O(1)
    while fst <= lst: # O(log(n)) - по сути бинарный поиск
        mid = (lst-fst + 1) // 2
        if not listt[mid][0]:
            mas_false.append(listt[fst:mid+1])
            fst = mid + 1
        else:
            mas_true.append(listt[mid:lst+1])
            lst = mid - 1
    return f'Пользователи, которым запрещено пользоваться ресурсом:\n {[mas_false]}\n Пользователи, которым' \
           f' разрешено пользоваться ресурсом:\n {mas_true}]'


@decor
def check_opt(listt):
    listt.sort() # O(n*log(n))
    fst = 0
    lst = len(listt) - 1 # O(1)
    mid_saved = 0
    while fst <= lst: # O(log(n)) - по сути бинарный поиск
        mid = (lst-fst + 1) // 2
        if not listt[mid][0]:
            fst = mid + 1
        else:
            lst = mid - 1
            mid_saved = mid
    return f'Пользователи, которым запрещено пользоваться ресурсом:\n {listt[:mid_saved]}\n Пользователи, которым' \
           f' разрешено пользоваться ресурсом:\n {listt[mid_saved:]}]'


print(check([[True, 'logdddin1', '2342'], [False, 'logixxn1', '2342'], [True, 'logxxvin1', '2342'], [True, '23675', 'loggg']]))
print('-----------------------------')
print(check_opt([[True, 'logdddin1', '2342'], [False, 'logixxn1', '2342'], [True, 'logxxvin1', '2342'], [True, '23675', 'loggg']]))

# Убрали отдельные массивы mas_true и mas_false, просто запомнив с какого элемента начинаются элементы с True. Тем
# самым экономим память.