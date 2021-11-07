"""
Создайте собственный класс-исключение, обрабатывающий ситуацию деления на ноль.
Проверьте его работу на данных, вводимых пользователем.
При вводе нуля в качестве делителя программа должна корректно обработать эту ситуацию и не завершиться с ошибкой.
"""

class Division(Exception):
    def __init__(self, num):
        self.num = num

try:
    numerator = int(input('Укажите числитель: '))
    denominator = int(input('Укажите знаменатель: '))
    if denominator == 0:
        raise Division('Делить на ноль нельзя')
except ValueError:
    print('Вы ввели не число')
except Division as div:
    print(div)
else:
    print(f'Результат деления = {numerator / denominator}')
