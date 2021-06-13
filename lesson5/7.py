import json


firms = {}

try:
    f = open("text_7.txt", "r", encoding="utf-8")
except IOError:
    print("Файл не существует")
else:
    for firm in f:
        firm_list = firm.split()
        firms[firm_list[0]] = int(firm_list[2]) - int(firm_list[3])
    f.close()

summa = 0
i = 0
for firm in firms.values():
    if firm >= 0:
        summa += firm
        i += 1

average = summa / i

with open("text_7_new.json", "w", encoding="utf-8") as f:
    json.dump([firms, {"average_profit": average}], f)
