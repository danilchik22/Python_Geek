from memory_profiler import profile


@profile
def fac(number):
    def factorial(number):
        if number == 1:
            return 1
        return number * (factorial(number - 1))

    return factorial(number)


print(fac(5))


# Проблема при профилировании рекурсивных функций заключается в том, что при каждом вызове функции выводится информация
# о потребляемой памяти, так как функция многократно вызывает сама себя. Решается вопрос оберткой функции другой
# функцией, которую уже в свою очередь профилируем.