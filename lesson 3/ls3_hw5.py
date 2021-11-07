def number():
    number = 0
    while True:
        n = input('Введите несколько чисел через пробел.\nДля завершения введите "*".\nВвод чисел: ').split()
        num = 0
        for i in n:
            if i != '*':
                num += int(i)
            else:
                break
        number += num
        print(number)
        if '*' in n:
            break
number()