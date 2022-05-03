import re


class Date:
    date = ""

    def __init__(self, date):
        Date.validation(date)
        Date.date = date

    @classmethod
    def extract(cls):
        number, month, year = map(int, re.split(r"[\.\\ ]+", cls.date))
        return [number, month, year]

    @staticmethod
    def validation(line):
        if not re.fullmatch(r"[0-9]{1,2}[\.\\ ]{1}[0-9]{1,2}[\.\\ ]{1}[0-9]{1,4}", line):
            raise ValueError("Неверная дата")
        else:
            number, month, year = map(int, re.split(r"[\.\\ ]+", line))
            if number == 0 or month == 0:
                raise ValueError("Неверная дата")
            else:
                if month == 2:
                    if year % 4 == 0:
                        if number > 29:
                            raise ValueError("Неверная дата")
                    else:
                        if number > 28:
                            raise ValueError("Неверная дата")
                else:
                    if month % 2 != 0:
                        if number > 31:
                            raise ValueError("Неверная дата")
                    else:
                        if number > 30:
                            raise ValueError("Неверная дата")
                if month > 12:
                    raise ValueError("Неверная дата")


d = Date("24.2.1956")
print(Date.extract())