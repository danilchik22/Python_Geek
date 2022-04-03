from random import choice


def get_jokes(n, flag=True):
    """This Function creates jokes from three words, which takes place in three array. Flag means that it's allowed or
     prohibited replays in the same Joke. Default flag is True"""
    nouns = ["автомобиль", "лес", "огонь", "город", "дом"]
    adverbs = ["сегодня", "вчера", "завтра", "позавчера", "ночью"]
    adjectives = ["веселый", "яркий", "зеленый", "утопичный", "мягкий"]
    result = []
    if flag:
        for index in range(n):
            result.append(choice(nouns) + " " + choice(adverbs) + " " + choice(adjectives))
        return result
    else:
        for index in range(n):
            if len(result) == 5:
                break
            word_nouns = choice(nouns)
            nouns.remove(word_nouns)
            word_adverbs = choice(adverbs)
            adverbs.remove(word_adverbs)
            word_adjectives = choice(adjectives)
            adjectives.remove(word_adjectives)
            result.append(word_nouns + " " + word_adverbs + " " + word_adjectives)
        return result


print(get_jokes(n=5, flag=False))
