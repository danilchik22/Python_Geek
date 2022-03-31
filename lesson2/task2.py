numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
list_words = ['в', '5', 'часов', '17', 'минут', 'температура', 'воздуха', 'была', '+5', 'градусов']
list_words_result = list_words.copy()
count_insert = 0
for index_word in range(len(list_words)):
    flag = True  # Using this flag, we'll determine if element is number
    for letter in range(len(list_words[index_word])):
        if numbers.count(list_words[index_word][letter]) == 0:  # If there is at least one not figure - not number
            flag = False
            if letter == 0 and list_words[index_word][letter] == '+' and len(list_words[
                                                                                 index_word]) > 1:
                """ If it's the first element and it's '+' and there is symbols anymore, then it may the Number """
    if flag:
        list_words_result.insert(index_word + count_insert, '"') # индекс в result нужно увеличивать на количество предыдущих вставок
        count_insert += 1
        list_words_result.insert(index_word + count_insert + 1, '"')
        count_insert += 1
        if len(list_words[index_word]) == 1:
            list_words_result[index_word + count_insert-1] = '0' + list_words_result[index_word + count_insert-1]
result = ' '.join(list_words_result)
"""
The result is a string with spaces inside the quotes. To remove them, first we should to find which spaces
are inside the quotes and which are outside. To do this, we will use the "flag" variable, which will show
 what quotation mark had met. If flag is 0, then this is the first quotation mark, we remove the space in the next 
 character. If it's 1 - is the second quotation mark, remove the space in the previous character. If it's 2 -then we reset the flag.
 """
flag = 0
indexes_replace = []
for index_letter in range(len(result)):
    if flag == 0:
        if result[index_letter] == '"':
            indexes_replace.append(index_letter + 1)
            flag += 1
    elif flag == 1:
        if result[index_letter] == '"':
            indexes_replace.append(index_letter - 1)
            flag += 1
    else:
        flag = 0
result_without_space = ""
for index_letter in range(len(result)):
    if indexes_replace.count(index_letter) == 0:
        result_without_space += result[index_letter]
print(result_without_space)