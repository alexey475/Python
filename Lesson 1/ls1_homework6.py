a = int(input('Укажите результаты пробежки первого дня в км: '))
b = int(input('Укажите общий желаемый результат в км: '))
day = 0
result = a
print('Результат:')
while result < b:
    day += 1
    if day <= 1:
        print(f'{day}-й день: {result:.2f}')
    else:
        result += result * 0.1
        print(f'{day}-й день: {result:.2f}')

print(f'Ответ: на {day}-й день спортсмен достиг результата - не менее {b} км')