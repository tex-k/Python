seasons = {1: "зима", 2: "зима", 3: "весна", 4: "весна", 5: "весна", 6: "лето", 7: "лето", 8: "лето", 9: "осень",
           10: "осень", 11: "осень", 12: "зима"}

while True:
    try:
        month = int(input("Введите номер месяца: "))
        break
    except ValueError:
        print("Необходимо ввести число")

if month >= 1 and month <= 12:
    print(seasons[month])
else:
    print("Нет такого месяца")
   