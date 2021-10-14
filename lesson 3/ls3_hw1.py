#Вариант 1
def number():
    a = int(input('Введите число: '))
    b = int(input('Введите число: '))
    def num(a, b):
        try:
            sep = a / b
            return sep
        except ZeroDivisionError:
            return 'На 0 делить нельзя'
    return num(a, b)
n = number()
print(n)

#Вариант 2
def number():
    a = int(input('Введите число: '))
    b = int(input('Введите число: '))
    return num(a, b)
def num(a, b):
    try:
        sep = a / b
        return sep
    except ZeroDivisionError:
        return 'На 0 делить нельзя'
n = number()
print(n)