"""
Создать программный файл в текстовом формате, записать в него построчно данные, вводимые пользователем.
Об окончании ввода данных будет свидетельствовать пустая строка.
"""
name_file = input('Введите название файла: ')
file = open(name_file, 'w')
while True:
    s = input('Введите данные: ')
    if s == '':
        break
    else:
        file.write(s + '\n')
file.close()
