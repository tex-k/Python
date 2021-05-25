first_result = int(input("Введите результат первого дня: "))
goal_result = int(input("Введите требуемый результат: "))

result = first_result
n = 1
while result < goal_result:
    n += 1
    result *= 1.1

print(f"Результат будет достигнут за {n} дней")
