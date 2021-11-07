products = [] #пронумерованные товары
analytics = {'название' : '', 'цена' : '', 'количество' : '', 'ед' : ''} #аналитика о товарах
check_new = ['Да', 'да', 'Нет', 'нет']
name_prod = []
price_prod = []
count_prod = []
unit_prod = []
number = 0
while True:
    new_product = input('Добавить новый товар? Введите "Да" или "Нет": ')
    if new_product not in check_new:
        continue
    elif new_product in (check_new[2], check_new[3]):
        break
    elif new_product in (check_new[0], check_new[1]):
        gds = {'название': '', 'цена': '', 'количество': '', 'ед': ''}
        name = input('Название товара: ')
        gds['название'] = name
        name_prod.append(name) #заполнение аналитики
        price = input('Цена: ')
        gds['цена'] = price
        price_prod.append(price) #заполнение аналитики
        count = input('Количество: ')
        gds['количество'] = count
        count_prod.append(count) #заполнение аналитики
        unit = input('Единица измерения: ')
        gds['ед'] = unit
        unit_prod.append(unit) #заполнение аналитики
        number += 1
        prod = (number), gds
        products.append(prod)
analytics['название'] = name_prod
analytics['цена'] = price_prod
analytics['количество'] = count_prod
analytics['ед'] = unit_prod
print(f'Список товаров: {products}')
print(f'Аналитика: {analytics}')
