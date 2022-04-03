def num_translate(number):
    """This Function translates words from English into Russian only in lowercase"""
    numbers = {
        'one': 'один',
        'two': 'два',
        'three': 'три',
        'four': 'четыре',
        'five': 'пять',
        'six': 'шесть',
        'seven': 'семь',
        'eight': 'восемь',
        'nine': 'девять',
        'ten': 'десять'
    }
    if number in numbers.keys():
        return numbers[number]
    else:
        return None


print(num_translate('two'))
