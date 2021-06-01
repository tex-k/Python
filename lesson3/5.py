s = 0
wrong_value = False
stop = False
while not stop:
    list_inner = input("Введите числа через пробелы (или * для завершения): ").split()
    list_final = []
    for num in list_inner:
        if num == "*":
            stop = True
            break
        try:
            list_final.append(float(num))
        except ValueError:
            wrong_value = True
            continue
    if wrong_value:
        print("Необходимо вводить числа")
        wrong_value = False
    s += sum(list_final)
    print(f"Сумма: {s}")