class Stationery:
    def __init__(self, title):
        self.title = title

    def draw(self):
        print("Запуск отрисовки...")


class Pen(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки. Предмет: {self.title}")


class Pencil(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки. Предмет: {self.title}")


class Handle(Stationery):
    def __init__(self, title):
        super().__init__(title)

    def draw(self):
        print(f"Запуск отрисовки. Предмет: {self.title}")


if __name__ == "__main__":
    handle = Handle("Маркер")
    pen = Pen("Ручка")
    pencil = Pencil("Карандаш")
    handle.draw()
    pen.draw()
    pencil.draw()
