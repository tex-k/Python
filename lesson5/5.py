with open("text_5.txt", "w", encoding="utf-8") as f:
    while True:
        try:
            number = input("Введите число или Enter для остановки: ")
            if number == "":
                break
            number = int(number)
        except ValueError:
            print("Необходимо ввести число")
        else:
            f.write(f"{number} ")

with open("text_5.txt", "r", encoding="utf-8") as f:
    numbers = f.read().split()

summa = 0
for n in numbers:
    summa += int(n)

print(summa)
