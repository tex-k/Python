def fact(n):
    factorial = 1
    for el in range(1, n + 1):
        factorial *= el
        yield factorial


while True:
    try:
        n = int(input("Введите целое положительное число: "))
        if n <= 0:
            print("Необходимо положительное число")
        else:
            break
    except ValueError:
        print("Необходимо целое число")

i = 0
for el in fact(n):
    i += 1
    print(f"{i}! = {el}")