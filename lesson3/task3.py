def thesaurus(*args):
    employees = {}
    for name_argv in args:
        list_name = employees.get(name_argv[0])
        if list_name is not None:
            list_name = employees[name_argv[0]]
            list_name.append(name_argv)
            employees[name_argv[0]] = list_name
        else:
            list_name = [name_argv]
            employees[name_argv[0]] = list_name
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
employees_sorted = dict(sorted(dict_employees.items()))
print(employees_sorted)
