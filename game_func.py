def check_letter(letter, word, hide_word):
    i = 0
    for word_letter in word:
        if word_letter == letter:
            hide_word = hide_word[:i] + letter + hide_word[i + 1:]
        i += 1
    return hide_word