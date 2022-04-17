list_tuple = []
with open("log.txt", "r") as f:
    line = f.readline()
    while line:
        tuple_web = (line.split(" ")[0], line.split(" ")[5].replace('"', ""), line.split(" ")[6])
        list_tuple.append(tuple_web)
        line = f.readline()
"""В консоли мы не можем увидеть все элементы, потому что после вывода части информации, консоль обновляется:"""
for el in list_tuple:
    print(el)
"""Попробуем вывести, к примеру, 834й элемент нашего списка кортежей:"""
print(f"Выводим 834й элемент: {list_tuple[834]}")
"""Он будет сопадать с 835-ым элементом нашего файла. Все верно"""