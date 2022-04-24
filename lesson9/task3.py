class Worker:
    def __init__(self, name, surname, position, income):
        self.name = name
        self.surname = surname
        self.position = position
        self._income = income


class Position(Worker):
    def __init__(self, name, surname, position, income):
        super().__init__(name, surname, position, income)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return int(self._income["wage"]) + int(self._income["bonus"])


if __name__ == "__main__":
    programmer = Position("Danil", "Gushchin", "Programmer", {"wage": 70000, "bonus": 30000})
    print(programmer.name)
    print(programmer.surname)
    print(programmer.position)
    print(programmer._income)
    print("-----------------------------------")
    print(f"{programmer.get_full_name()}\nЗарплата: {programmer.get_total_income()} ")
