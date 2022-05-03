import re


class Store:
    count_things = 0
    dict_things = {}

    def __init__(self, name):
        self.name = name

    def acceptance_one(self, obj):
        self.count_things += 1
        if obj.name in self.dict_things:
            list_things = self.dict_things[obj.name]
            list_things.append(obj)
            self.dict_things[obj.name] = list_things
        else:
            self.dict_things[obj.name] = [obj]

    def acceptance_many(self, list):
        map(self.acceptance_one, list)

    @staticmethod
    def validation(line):
        if line == "0":
            return None
        if re.fullmatch(r"[0-9]+", line):
            return int(line)
        else:
            raise ValueError("Ввели не число")

    def __str__(self):
        line = f"---------------------\nВсего единиц на складе: {self.count_things} \nНа складе следующие товары:\n"
        for name, thing in self.dict_things.items():
            line = line + f"{name}: {len(thing)} штук\n"
        return line


class OfficeEquipment:

    def __init__(self, name, price, weight):
        self.name = name
        self.price = price
        self.weight = weight


class Printer(OfficeEquipment):

    def __init__(self, price=None, weight=None, print_speed=None, resource=None):
        super().__init__("Принтер", price, weight)
        self.print_speed = print_speed
        self.resource = resource


class Scanner(OfficeEquipment):

    def __init__(self, price=None, weight=None, memory_mb=None):
        super().__init__("Сканнер", price, weight)
        self.memory_mb = memory_mb


class Xerox(OfficeEquipment):

    def __init__(self, price=None, weight=None, count_copy=None):
        super().__init__("Ксерокс", price, weight)
        self.count_copy = count_copy


st = Store("Склад1")
while True:
    name = input("Введите название оргтехники на английском (либо 'stop' - для остановки): ")
    if name == "stop":
        break
    if name not in [name.__name__ for name in OfficeEquipment.__subclasses__()]:
        print("Такую технику не принимаем на склад")
        continue
    price = Store.validation(input("Введите цену оргтехники в рублях: (если неизвестно - 0): "))
    weight = Store.validation(input("Введите вес оргтехники в граммах: (если неизвестно - 0): "))
    if name == "Printer":
        print_speed = Store.validation(input("Введите скорость печати принтера (если неизвестно - 0): "))
        resource = Store.validation(input("Введите ресурс принтера, кол-во страниц: (если неизвестно - 0): "))
        count = Store.validation(input("Введите число принтеров для загрузки на склад: "))
        for i in range(count):
            pr = Printer(price, weight, print_speed, resource)
            st.acceptance_one(pr)

    elif name == "Scanner":
        memory_mb = Store.validation(input("Введите количество памяти сканера в мегабайтах (если неизвестно - 0): "))
        count = Store.validation(input("Введите число сканеров для загрузки на склад: "))
        for i in range(count):
            pr = Scanner(price, weight, memory_mb)
            st.acceptance_one(pr)
    elif name == "Xerox":
        count_copy = Store.validation(input("Введите количество копий в минуту у сканера (если неизвестно - 0): "))
        count = Store.validation(input("Введите число ксероксов для загрузки на склад: "))
        for i in range(count):
            pr = Xerox(price, weight, count_copy)
            st.acceptance_one(pr)
    else:
        print("Такую технику не принимаем на склад")
print(st)
