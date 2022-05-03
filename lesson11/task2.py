class ExceptionZero(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == "__main__":
    data = int(input("Введите число: "))
    if data == 0:
        raise ExceptionZero("ДЕЛЕНИЕ НА НОЛЬ!!!")
    else:
        print(f"Результат: {3 / data}")
