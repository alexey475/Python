"""
Реализовать скрипт, в котором должна быть предусмотрена функция расчёта заработной платы сотрудника.
Используйте в нём формулу: (выработка в часах*ставка в час) + премия.
Во время выполнения расчёта для конкретных значений необходимо запускать скрипт с параметрами.
"""
from sys import argv
name, work_time, rate_time, bonus = argv
a = int(work_time)
b = int(rate_time)
c = int(bonus)
def salary(a, b, c):
    result = a * b + c
    print(f'Заработная плата сотрудника {result}')
s = salary(a, b, c)
