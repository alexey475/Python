def my_func(a, b ,c):
    func = []
    for i in (a, b ,c):
        func.append(i)
    func.sort()
    result = func[1] + func[2]
    return result
f = my_func(25, 5 ,10)
print(f)
