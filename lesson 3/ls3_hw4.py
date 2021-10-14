#Вариант 1
def my_func1(x, y):
    result = x**y
    return result
print(my_func1(5, 3))

#Вариант 2
def my_func2(x, y):
    i = 0
    result = 1
    while i < y:
        result = result * x
        i += 1
    return result
print(my_func2(5, 3))