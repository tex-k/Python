num = int(input("Введите целое положительное число: "))

max_n = 0
while num:
    n = num % 10
    if n > max_n:
        max_n = n
    num = num // 10

print(max_n)
