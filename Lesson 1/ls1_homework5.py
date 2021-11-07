income = int(input('Укажите значение выручки: '))
cost = int(input('Укажите издержки: '))
if income < cost:
    print('Издержки больше выручки')
elif income == cost:
    print("Фирма работает в ноль")
else:
    number = int(input('Укажите численность сотрудников: '))
    rent = ((income - cost) / income) * 100 #рентабельность
    profit_employ = (income - cost) / number
    print(f'Выручка больше издержек\nРентабельность {rent}%\nПрибыль фирмы в расчете на одного сотрудника {profit_employ:.2f}')
