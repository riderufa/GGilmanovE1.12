import random

from game_func import random_word, change_hide_word, change_errors_count, change_errors_text

words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']
word = random_word(words)
# print(word)

print('Угадайте слово из {} букв.'.format(len(word)))
hide_word = '_' * len(word)
errors_count = 0
end_print = 'Поздравляем!'

while '_' in hide_word:
    print(hide_word)
    letter = str(input())
    if letter in word:
        hide_word = change_hide_word(letter, word, hide_word)
    else:
        errors_count = change_errors_count(errors_count)
        errors_text = change_errors_text(errors_count)
        print('{} {}'.format(errors_count, errors_text))
    if errors_count > 3:
        end_print = 'Четыре ошибки. Игра окончена.'
        break

print(end_print)

