# Сложность алгоритма O(n):
def check(dictt):
    for key, value in dictt.items():  # O(n)
        if value[1]:  # O(1)
            print(f'Пользователь {key} может пользоваться ресурсом')  # O(1)
        else:
            print(f'Пользователю {key} нужно пройти активацию профиля.')  # O(1)


check({'login1': ['2342', False], 'loggg': ['23675', True]})


# Сложность алгоритма O(n*log(n))

def check2(listt):
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


print(check2([[True, 'logdddin1', '2342'], [False, 'logixxn1', '2342'], [True, 'logxxvin1', '2342'], [True, '23675', 'loggg']]))

# Первый способ эффективнее, потому что сложность алгоритмы O(n)