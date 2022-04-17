import sys
dict_people = {}
with open("People.txt", "r", encoding="utf-8") as file_people:
    with open("Hobby.txt", "r", encoding="utf-8") as file_hobby:
        line_people = file_people.readline()
        line_hobby = file_hobby.readline()
        while line_people:
            #Ключом должен быть неизменяемый тип, поэтому выбрали именно кортеж, к тому же фио часто не меняется у людей
            key = tuple(line_people.rstrip().split(","))
            if line_hobby:
                # Значением может быть любой тип, хобби могут дополняться, поэтому выбираем список.
                value = line_hobby.rstrip().split(",")
            else:
                value = None
            dict_people[key] = value
            line_people = file_people.readline()
            line_hobby = file_hobby.readline()
    if line_hobby:
        sys.exit([1])
    else:
        print(dict_people)
