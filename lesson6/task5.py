import sys
import json
dict_people = {}
with open(sys.argv[1], "r", encoding="utf-8") as file_people:
    with open(sys.argv[2], "r", encoding="utf-8") as file_hobby:
        line_people = file_people.readline()
        line_hobby = file_hobby.readline()
        while line_people:
            key = tuple(line_people.rstrip().split(","))
            if line_hobby:
                value = line_hobby.rstrip().split(",")
            else:
                value = None
            dict_people[key] = value
            line_people = file_people.readline()
            line_hobby = file_hobby.readline()
    if line_hobby:
        sys.exit([1])
    else:
        with open(sys.argv[3], "w") as file_result:
            # В json файлах ключом не может быть кортеж, поэтому переводим ключи в строку
            dict_people = {" ".join(people) : hobby for people, hobby in dict_people.items()}
            json.dump(dict_people, file_result)