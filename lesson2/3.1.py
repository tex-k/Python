seasons = ["зима", "зима", "весна", "весна", "весна", "лето", "лето", "лето", "осень", "осень", "осень", "зима"]

while True:
    try:
        month = int(input("Введите номер месяца: "))
        break
    except ValueError:
        print("Необходимо ввести число")

if month >= 1 and month <= 12:
    print(seasons[month - 1])
else:
    print("Нет такого месяца")
