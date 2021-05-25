proceeds = float(input("Введите величину выручки: "))
costs = float(input("Введите величину издержек: "))

if proceeds > costs:
    profitability = round((proceeds - costs) / proceeds * 100)
    print("Фирма работает с прибылью")
    print(f"Рентабельность: {profitability}%")
    employees = int(input("Введите количество сотрудников: "))
    profit_employee = (proceeds - costs) / employees
    print(f"Прибыль на одного сотрудника: {profit_employee:.2f}")
else:
    print("Фирма работает с убытками")
