goods = []

i = 0
while True:
    name = input("Введите название нового товара или stop: ")
    if name == "stop":
        break
    while True:
        try:
            price = int(input("Введите цену: "))
            break
        except ValueError:
            print("Цена должна быть числом")
    while True:
        try:
            amount = int(input("Введите количество: "))
            break
        except ValueError:
            print("Количество должно быть числом")
    units = input("Введите единицы измерения: ")
    i += 1
    goods.append((i, {"название": name, "цена": price, "количество": amount, "ед": units}))

analiyics = {"название": [], "цена": [], "количество": [], "ед": []}

for elem in goods:
    analiyics["название"].append(elem[1]["название"])
    analiyics["цена"].append(elem[1]["цена"])
    analiyics["количество"].append(elem[1]["количество"])
    analiyics["ед"].append(elem[1]["ед"])

analiyics["название"] = list(set(analiyics["название"]))
analiyics["цена"] = list(set(analiyics["цена"]))
analiyics["количество"] = list(set(analiyics["количество"]))
analiyics["ед"] = list(set(analiyics["ед"]))

print(analiyics)
