"""
Создать (программно) текстовый файл, записать в него программно набор чисел, разделённых пробелами.
Программа должна подсчитывать сумму чисел в файле и выводить её на экран.
"""
with open('hw5.txt', 'w') as hw5:
    num = input('Введите числа через пробел: ')
    hw5.writelines(num)
with open('hw5.txt', 'r') as hw5:
    my_list = [i.split() for i in hw5]
    print(my_list)
    result = sum(map(int, my_list[0]))
    print(result)