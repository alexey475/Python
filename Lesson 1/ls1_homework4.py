number = abs(int(input("Введите целое положительное число: ")))
max = number % 10
while True:
    number = number // 10
    if number % 10 > max:
        max = number % 10
    elif number > 9:
        continue
    else:
        print("Максимальное число: ", max)
        break
