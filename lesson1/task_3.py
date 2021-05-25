n = input("Введите целое число: ")

summ = 0
i = 1
while i <= 3:
    j = 1
    num = ""
    while j <= i:
        num += n
        j += 1
    summ += int(num)
    i += 1

print(summ)
