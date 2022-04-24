class Car:
    def __init__(self, speed, color, name, isPolice):
        if speed < 0:
            raise ValueError("Скорость не может быть меньше 0")
        else:
            self.speed = speed
        self.color = color
        self.name = name
        self.isPolice = isPolice

    def go(self):
        print(f"{self.name} поехала")

    def stop(self):
        print(f"{self.name} остановилась")

    def turn(self, direction):
        print(f"{self.name} повернула {direction}")

    def show_speed(self):
        print(f"Текущая скорость: {self.speed}.")

    def __str__(self):
        return f"Марка машины: {self.name}. Скорость машины: {self.speed}. Цвет машины: {self.color}. " \
               f"Полицейская это машина? {self.isPolice}"


class TownCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 40:
            print(f"Текущая скорость {self.name}: {self.speed}. Превышение скорости.")
        else:
            print(f"Текущая скорость {self.name}: {self.speed}")


class WorkCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)

    def show_speed(self):
        if self.speed > 60:
            print(f"Текущая скорость {self.name}: {self.speed}. Превышение скорости.")
        else:
            print(f"Текущая скорость {self.name}: {self.speed}")


class SportCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, False)


class PoliceCar(Car):
    def __init__(self, speed, color, name):
        super().__init__(speed, color, name, True)


if __name__ == "__main__":
    police = PoliceCar(90, "красный", "Renault")
    sportcar = SportCar(149, "белый", "Infiniti")
    workercar = WorkCar(90, "красный", "Волга")
    towncar = TownCar(34, "зеленый", "Nissan")
    print(police)
    print(sportcar)
    print(workercar)
    print(towncar)
    police.turn("Направо")
    towncar.go()
    workercar.show_speed()
    sportcar.stop()
    towncar.show_speed()
