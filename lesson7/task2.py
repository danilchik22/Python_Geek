import os
"""Структура файла yaml будет следующая: каждая следующая ветвь иерархии отделяется 4 пробелами"""
with open("config.yaml", "r", encoding="utf-8") as f:
    line = f.readline()
    space = "    "
    list_str = []
    while line:
        #Создадим список словарей, состоящих из файла/директории и его глубины иерархии
        deep_dir = 0
        while line.startswith(space):
            deep_dir += 1
            line = line[4:]
        list_str.append({line.rstrip():deep_dir})
        line = f.readline()
    path_file = ""
    count = 0
    #для каждой записи нашего списка нужно сформировать свой путь в иерархии
    #проходим с конца в начало, сравниваем глубину иерархии с каждым следующим элементом
    #если глубина ирерархии меньше, то этот ближайший элемент - родительский
    for dict_str in list_str[:0:-1]:
        count+=1
        deep1 = [i for i in dict_str.values()][0]
        path_file = ""
        # всегда идем от текущей точки вверх
        for other_str in list_str[-count::-1]:
            deep2 = [i for i in other_str.values()][0]
            if deep2 < deep1:
                k = [i for i in other_str.keys()][0]
                path_file = os.path.join(k, path_file)
                deep1 = deep2
        if not os.path.exists(path_file):
            os.makedirs(path_file)
        #формируем полный путь файла
        path_file = os.path.join(path_file, [i for i in dict_str.keys()][0])
        #если это файл, то создаем его
        if path_file.endswith(".py") or path_file.endswith(".html"):
            t = open(path_file, "w")
        else:
            #если это папка, то создаем ее, если она уже не создана
            if not os.path.exists(path_file):
                os.makedirs(path_file)



