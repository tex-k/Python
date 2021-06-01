def my_func(x, y):
    result = 1
    for i in range(abs(y)):
        result *= x
    return 1 / result


while True:
    x = input("Введите действительное положительное число: ")
    try:
        x = float(x)
    except ValueError:
        print("Нужно ввести число")
    else:
        if x > 0:
            break
        print("Число должно быть положительным")

while True:
    y = input("Введите целое отрицательное число: ")
    try:
        y = float(y)
    except ValueError:
        print("Нужно ввести число")
    else:
        if y < 0:
            if y == int(y):
                y = int(y)
                break
            print("Число должно быть целым")
        else:
            print("Число должно быть отрицательным")

print(my_func(x, y))