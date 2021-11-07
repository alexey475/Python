"""
Создать текстовый файл (не программно), сохранить в нём несколько строк, выполнить подсчёт строк и слов в каждой строке.
"""
#Вариант 1
with open('hw2.txt', 'r') as hw2:
    count_str = 0
    s = 0
    for i in hw2:
        count_str += 1
        str = i.split()
        count_word = 0
        for el in str:
            count_word += 1
        s += count_word
        print(f'В строке №{count_str} количество слов = {count_word}')
    print(f'Всего строк = {count_str}')
    print(f'Всего слов = {s}')

#Вариант 2
with open('hw2.txt', 'r') as hw2:
    lines = [i for i in hw2 if i != '\n']
    print(f'Всего строк: {len(lines)}')
    word = 0
    for l in lines:
        word += len(l.split())
    print(f'Всего слов: {word}')
    for num, words in enumerate([len(l.split()) for l in lines], 1):
        print(f'В строке №{num} количество слов = {words}')
