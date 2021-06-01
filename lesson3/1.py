def f(nom, denom):
    return nom / denom


while True:
    nom = input("Введите числитель: ")
    try:
        nom = float(nom)
        break
    except ValueError:
        print("Числитель должен быть числом")

while True:
    denom = input("Введите знаменатель: ")
    try:
        denom = float(denom)
        break
    except ValueError:
        print("Знаменатель должен быть числом")

try:
    print(f(nom, denom))
except ZeroDivisionError:
    print("Деление на ноль")
