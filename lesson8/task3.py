def type_logger(funct):
    def wrapper(*args, **kwargs):
        print("Имя функции: " + funct.__name__)
        print("Позиционные аргументы:")
        if len(args) == 0:
            print("Нет")
        for arg in args:
            print(str(type(arg)) + ", ")
        print("Именованные аргументы:")
        if len(kwargs) == 0:
            print("Нет")
        for arg in kwargs.values():
            print(str(type(arg)) + ", ")
        print("Результат:")
        return funct(*args, **kwargs)
    return wrapper


@type_logger
def calc_square(x, weight):
    return x * weight


print(calc_square(3, weight = 34.5))
