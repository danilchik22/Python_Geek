src = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]
tmp = set()
result = []
for number in src:
    if number not in tmp:
        tmp.add(number)
    else:
        tmp.remove(number)
for number in src:
    if number in tmp:
        result.append(number)
print(result)