line = input("Введите строку: ").split()

for i, word in enumerate(line, 1):
    print(i, word[:10])
