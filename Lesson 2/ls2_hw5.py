#Вариант 1
my_list = [25, 19, 7, 5, 3, 3, 2]
print('Заданный рейтинг', my_list)
max_num = max(my_list)
min_num = min(my_list)
calculation = []
num = 0
new_elem = int(input('Введите новый элемент рейтинга: '))
for i in my_list:
    if i == new_elem: #новый элемент есть в списке
         my_list.insert(my_list.index(i), new_elem)
         break
    else: #нового элемента нет в списке
        if new_elem < min_num:
            my_list.append(new_elem)
            break
        elif new_elem > max_num:
            my_list.insert(my_list.index(max_num), new_elem)
            break
        elif new_elem > min_num and new_elem < max_num:
            for j in my_list:
                calculation.append(abs(j - new_elem))
            index_calculation = calculation.index(min(calculation))
            num = my_list[index_calculation]
            if num < new_elem:
                my_list.insert(my_list.index(num), new_elem)
                break
            elif num > new_elem:
                my_list.insert(my_list.index(num) + 1, new_elem)
                break
print('Новый рейтинг', my_list)

#Вариант 2
my_list1 = [25, 19, 7, 5, 3, 3, 2]
new_elem1 = int(input('Введите новый элемент рейтинга: '))
my_list1.append(new_elem1)
my_list1 = sorted(my_list1, reverse=True)
print(f'Новый рейтинг {my_list1}')