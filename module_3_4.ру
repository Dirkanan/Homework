def single_root_words(root_word, *other_words):
    same_words = []
    root_word_upper = root_word.upper()
    for i in other_words:
        other_words_upper = i.upper()
        if root_word_upper in other_words_upper or other_words_upper in root_word_upper:
            same_words.append(i)
    return same_words

result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)
