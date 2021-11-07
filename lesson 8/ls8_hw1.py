"""
Реализовать класс «Дата», функция-конструктор которого должна принимать дату в виде строки формата «день-месяц-год».
В рамках класса реализовать два метода. Первый, с декоратором @classmethod.
Он должен извлекать число, месяц, год и преобразовывать их тип к типу «Число».
Второй, с декоратором @staticmethod, должен проводить валидацию числа, месяца и года (например, месяц — от 1 до 12).
Проверить работу полученной структуры на реальных данных.
"""
class Date:
    def __init__(self, day, month, year):
        self.day = day
        self.month = month
        self.year = year

    @classmethod
    def number(cls, day_month_year):
        day, month, year = map(int, str(day_month_year).split('-'))
        return cls(day, month, year)

    @staticmethod
    def check_date(day, month, year):
        if 1 <= day <= 31:
            if 1 <= month <= 12:
                if 1 <= year <= 2021:
                    return f'Дата корректная'
                else:
                    return f'Неправильный год'
            else:
                return f'Неправильный месяц'
        else:
            return f'Неправильный день'

    def __str__(self):
        return f'Числовой тип {self.day, self.month, self.year}'


date1 = Date.number('12-10-2020')
print(date1)
print(date1.check_date(date1.day, date1.month, date1.year))