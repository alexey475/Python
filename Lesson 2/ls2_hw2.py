count = int(input('Введите количество элементов списка: '))
my_list = []
i = 0
check = 0
check = 1 if count % 2 == 0 else 2
while i < count:
    my_list.append(input('Введите следующий элемент для списка: '))
    i += 1
print('origin',my_list)

for el in range(0, len(my_list)-check, 2):
    my_list[el], my_list[el + 1] = my_list[el + 1], my_list[el]
print('revers', my_list)
