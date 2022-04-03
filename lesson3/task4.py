def thesaurus(*args):
    employees = {}
    for person_args in args:
        dict_firstname = employees.get(person_args.split(' ')[1][0])
        if dict_firstname is not None:
            list_names = dict_firstname.get(person_args.split(' ')[0][0])
            if list_names is not None:
                list_names.append (person_args)
                dict_firstname[person_args.split(' ')[0][0]] = list_names
                employees[person_args.split(' ')[1][0]] = dict_firstname
            else:
                dict_firstname[person_args.split(' ')[0][0]] = [person_args]
                employees[person_args.split(' ')[1][0]] = dict_firstname
        else:
            dict_firstname = {person_args.split(' ')[0][0]: [person_args]}
            employees[person_args.split(' ')[1][0]] = dict_firstname
    return employees


enter_employees = []
count = 1
enter = input(f"Введите {count}-го человека, либо введите 'Выход' для завершения ввода:\n")
enter_employees.append(enter)
while True:
    count += 1
    enter = input(f"Введите {count}-го человека, либо введите 'Выход' для завершения ввода:\n")
    if enter == "Выход":
        break
    enter_employees.append(enter)
dict_employees = thesaurus(*enter_employees)
employees_sorted = dict([(k, dict(sorted(v.items()))) for k,v in sorted(dict_employees.items())])
print(employees_sorted)
