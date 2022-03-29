number = int(input("Введите число: "))
if number % 10 == 1:
    print(f'{number} процент')
elif 1 < number % 10 < 5:
    print(f'{number} процента')
else:
    print(f'{number} процентов')