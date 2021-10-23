"""
Создать (не программно) текстовый файл со следующим содержимым:
One — 1
Two — 2
Three — 3
Four — 4
Напишите программу, открывающую файл на чтение и считывающую построчно данные.
При этом английские числительные должны заменяться на русские.
Новый блок строк должен записываться в новый текстовый файл.
"""
dictionary = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
ch_file = []
with open('hw4.txt', 'r', encoding = 'utf-8') as hw4:
    file = [i.split(' — ') for i in hw4]
    print(file)
    for i in file:
        if i[0] in dictionary:
            word = dictionary[i[0]]
            ch_file.append(word + ' — ' + i[1])
new_file = input('Укажите имя нового файла: ')
with open(new_file, 'w', encoding = 'utf-8') as new_file:
    new_file.writelines(ch_file)
