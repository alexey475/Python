def user(**kwargs):
    structure = []
    values = kwargs.values()
    for i in values:
        structure.append(i)
    return structure
p = user(name = 'Иван', surname = 'Иванов', year = '1995', city = 'Москва', email = 'ivanov@mail.ru', telefone = 12345)
print(p)