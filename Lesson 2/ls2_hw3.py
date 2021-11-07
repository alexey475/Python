season = None
monate = 0

while 0 >= monate or 12 < monate:
    monate = int(input('Укажите месяц от 1 до 12: '))
periods = {
    1 : 'Зима', 2 : 'Зима',
    3 : 'Весна', 4 : 'Весна', 5 : 'Весна',
    6 : 'Лето', 7 : 'Лето', 8 : 'Лето',
    9 : 'Осень', 10 : 'Осень', 11 : 'Осень',
    12 : 'Зима'
}
season = periods.get(monate)
print(f'Ответ: Время года {monate} месяца это {season}')
