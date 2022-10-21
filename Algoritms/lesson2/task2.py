def count_figures(number):
    if number//10 == 0:
        if number%2 == 0:
            return 1, 0
        else:
            return 0, 1
    if number%2 == 0:
        return count_figures(number//10)[0]+1, count_figures(number//10)[1]
    else:
        return count_figures(number // 10)[0], count_figures(number // 10)[1] + 1

number = int(input('Введите число: '))
count = count_figures(number)
print(f'Количество четных: {count[0]}. Количество нечетных: {count[1]}')