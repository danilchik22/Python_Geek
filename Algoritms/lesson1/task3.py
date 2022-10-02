# Сложность алгоритма O(n*log(n))
def search_company(dictt):
    if len(dictt) < 3:  # O(1)
        return None
    dictt = sorted(dictt.items(), key=lambda item: item[1])  # O(n * log(n))
    return dict(dictt[-3:])  # O(n)


dict1 = search_company({'com1': 345, 'comm': 10, 'com2': 456, 'com3': 9856, 'com4': 23, 'com5': 2332435})
print("Компании с наибольшей прибылью: ")
for key, value in dict1.items():
    print(f'Компания {key}. Прибыль: {value}')


# Алгоритм 2
# Сложность алгоритма O(n)

def search_company_2(dictt):
    if len(dictt) < 3:  # O(1)
        return None
    lst = list(dictt.values()) # O(n)
    max = [lst.pop(), lst.pop(), lst.pop()]  # O(1)
    max.sort(reverse=True) # O(1) - сортировка всего 3х элементов при любых n, поэтому O - константа.
    for i in lst: # O(n)
        for j in range(0, 3): # O(1) - цикл по 3м элементам всегда
            if i > max[j]:  # O(1)
                max[j] = i # O(1)
                break
    result = {}
    for key, value in dictt.items(): # O(n)
        for j in range(0, 3): # O(1)
            if value == max[j]: # O(1)
                result[key] = value # O(1)
    return result


dict2 = search_company_2({'com1': 345, 'comm': 10, 'com2': 456, 'com3': 9856, 'com4': 23, 'com5': 2332435})
print("Компании с наибольшей прибылью: ")
for key, value in dict2.items():
    print(f'Компания {key}. Прибыль: {value}')