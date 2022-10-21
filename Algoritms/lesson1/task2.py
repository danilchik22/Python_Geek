# Сложность алгоритма O(n*n):

def search_min(lst):
    if not lst:
        return None
    for i in range(0, len(lst)):
        for j in range(i, len(lst)):
            if lst[i] > lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    return lst[0]


print(search_min([56, 34, 12, 10, 2, 45, 78, 32]))


# Сложность алгоритма O(n):

def search_min2(lst):
    if not lst:
        return None
    min = lst[0]
    for i in lst:
        if i < min:
            min = i
    return min


print(search_min2([56, 34, 12, 10, 2, 45, 78, 32]))
