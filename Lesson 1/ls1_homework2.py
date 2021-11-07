seconds = int(input('Введите время в секундах: '))
hour = seconds // 3600
minute = (seconds % 3600) // 60
second = (seconds % 3600) % 60
print(f'{hour}:{minute}:{second}')