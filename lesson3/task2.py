def num_translate_adv(number):
    """ This Function translates Words from English into Russian, including uppercase"""
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
    if number.lower() == number:
        if number in numbers.keys():
            return numbers[number]
        else:
            return None

    else:
        if number.lower() in numbers.keys():
            return numbers[number.lower()].capitalize()
        else:
            return None


print(num_translate_adv('One'))
