import hashlib


def unique_substring(word):
    substrings = set()
    for i in range(0, len(word)):
        for j in range(0, len(word)):
            substrings.add(hashlib.sha256(word[i:j].encode()).hexdigest())
    return len(substrings)


if __name__ == '__main__':
    our_word = input('Введите слово: ')
    print(f'Количество подстрок: {unique_substring(our_word)}')
    