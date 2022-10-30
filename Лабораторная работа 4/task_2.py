def get_count_char(str_):
    vocab = {}
    for symbol in str_:
        if symbol.isalpha():
            low_symbol = symbol.lower()
            if vocab.get(low_symbol) is not None:
                vocab.update({low_symbol: vocab.get(low_symbol) + 1})
            else:
                vocab[low_symbol] = 1
    return vocab


def get_percent_char(words):
    vocab = {}
    sum_symbol = 0

    for keys in words:
        sum_symbol += words.get(keys)

    for keys in words:
        vocab.update({keys: words.get(keys) / sum_symbol * 100})

    return vocab


main_str = """
    Данное предложение будет разбиваться на отдельные слова. 
    В качестве разделителя для встроенного метода split будет выбран символ пробела. На выходе мы получим список отдельных слов. 
    Далее нужно отсортировать слова в алфавитном порядке, а после сортировки склеить их с помощью метода строк join. Приступим!!!!
"""
print(get_count_char(main_str))
