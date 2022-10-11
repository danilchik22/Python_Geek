def do_operation():
    sign = input('Введите знак операции: ')
    if sign == '0':
        return
    if sign != '0' and sign != '+' and sign != '/' and sign != '-' and sign != '*':
        print('Ввод не корректен. Введите заново.')
        do_operation()
    enter_number1 = input('Введите 1-е число: ')
    if enter_number1.isdigit():
        number1 = int(enter_number1)
        enter_number2 = input('Введите 2-е число: ')
        if enter_number2.isdigit():
            number2 = int(enter_number2)
            if number2 == 0 and sign == '/':
                print('На ноль делить нельзя. Введите другое число')
                do_operation()
            if sign == '+':
                print(f'Ваш результат {number1 + number2}')
            if sign == '-':
                print(f'Ваш результат {number1 - number2}')
            if sign == '*':
                print(f'Ваш результат {number1 * number2}')
            if sign == '/':
                print(f'Ваш результат {number1 / number2}')
            do_operation()
        else:
            print('Вы ввели не число. Введите все заново.')
            do_operation()
    else:
        print('Вы ввели не число. Введите все заново.')
        do_operation()


if __name__ == '__main__':
    do_operation()

