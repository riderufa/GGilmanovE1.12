import random

def random_word(words):
    word = random.choice(words)
    return word

def insert_letter(hide_word, letter, i):
    hide_word = hide_word[:i] + letter + hide_word[i + 1:]
    return hide_word

def change_hide_word(letter, word, hide_word):
    for i, word_letter in enumerate(word):
        if word_letter == letter:
            hide_word = insert_letter(hide_word, letter, i)
    return hide_word

def change_errors_count(errors_count):
    errors_count += 1
    return errors_count

def change_errors_text(errors_count):
    if errors_count == 1:
        errors_text = 'ошибка' 
    else:
        errors_text = 'ошибки'
    return errors_text