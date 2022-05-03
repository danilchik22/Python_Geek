import re


class CheckNumbers(Exception):
    def __init__(self, txt):
        self.txt = txt


if __name__ == "__main__":
    list_numbers = []
    while True:
        try:
            number = input("Введите число: ")
            if number == "stop":
                break
            else:
                if re.fullmatch(r"([0-9]+[\.,]{1}[0-9]+)", number):
                    number = number.replace(",", ".")
                    list_numbers.append(float(number))
                elif re.fullmatch(r"[0-9]+", number):
                    list_numbers.append(int(number))
                else:
                    raise CheckNumbers("Это не число!!")
        except CheckNumbers:
            print("Вы ввели не число")
    print(list_numbers)