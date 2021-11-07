text = input('Ведите несколько слов: ').split()
for i in enumerate(text, 1):
    i = i[:10]
    print(i)