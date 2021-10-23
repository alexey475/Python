"""
Создать вручную и заполнить несколькими строками текстовый файл, в котором каждая строка будет содержать данные о фирме:
название, форма собственности, выручка, издержки.
Пример строки файла: firm_1   ООО   10000   5000.
Необходимо построчно прочитать файл, вычислить прибыль каждой компании, а также среднюю прибыль.
Если фирма получила убытки, в расчёт средней прибыли её не включать.
Далее реализовать список. Он должен содержать словарь с фирмами и их прибылями, а также словарь со средней прибылью.
Если фирма получила убытки, также добавить её в словарь (со значением убытков).
Пример списка: [{“firm_1”: 5000, “firm_2”: 3000, “firm_3”: 1000}, {“average_profit”: 2000}].
Итоговый список сохранить в виде json-объекта в соответствующий файл.
Пример json-объекта:
[{"firm_1": 5000, "firm_2": 3000, "firm_3": 1000}, {"average_profit": 2000}]
Подсказка: использовать менеджер контекста
"""
import json

list_firm = []
dict_firm = {}
dict_profit = {"average_profit": None}
profit = 0
n = 0 #число компаний для расчета средней прибыли
with open('hw7.txt', 'r', encoding = 'utf-8') as hw7:
    file = [i.split() for i in hw7]
for i in file:
    dict_firm[i[0]] = int(i[2]) - int(i[3])
    if dict_firm[i[0]] > 0:
        profit += dict_firm[i[0]]
        n += 1
dict_profit["average_profit"] = profit / n
list_firm.append(dict_firm)
list_firm.append(dict_profit)
print(list_firm)
js_file = input('Укажите имя файла с расширением json: ')
while list(js_file[-5:]) != list('.json'):
    js_file = input('Укажите имя файла с расширением json: ')
with open(js_file, 'w') as js_file:
    json.dump(list_firm, js_file)