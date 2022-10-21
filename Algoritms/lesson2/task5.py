def output_list_asii(min, max):
    if max == min:
        print(f'{str(min)} - {chr(min)}', end=' ')
        return 1
    count = output_list_asii(min, max - 1)
    if count % 10 == 0:
        print('\n')
    print(f'{str(max)} - {chr(max)}', end=' ')
    return count + 1


if __name__ == '__main__':
    min_range = int(input('Введите нижнюю границу диапазона: '))
    max_range = int(input('Введите верхнюю границу диапазона: '))
    output_list_asii(min_range, max_range)
