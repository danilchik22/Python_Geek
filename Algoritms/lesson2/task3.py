def reverse_number(number):
    if number // 10 == 0:
        return number
    return str(number % 10) + str(reverse_number(number // 10))


if __name__ == '__main__':
    print(reverse_number(344322232350))
