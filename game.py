import random

words = ['skillfactory', 'testing', 'blackbox', 'pytest', 'unittest', 'coverage']

word = random.choice(words)
# print(word)

print('Угадайте слово из {} букв.'.format(len(word)))
hide_word = '_' * len(word)
errors_count = 0
print(hide_word)
end_print = 'Поздравляем!'
while '_' in hide_word:
    letter = str(input())
    i = 0
    if letter in word:
        for word_letter in word:
            if word_letter == letter:
                hide_word = hide_word[:i] + letter + hide_word[i + 1:]
            i += 1
    else:
        errors_count += 1
        print('{} ошибки'.format(errors_count))
    print(hide_word)
    if errors_count > 3:
        end_print = 'Четыре ошибки. Игра окончена.'
        break
print(end_print)