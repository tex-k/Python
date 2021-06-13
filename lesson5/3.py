try:
    f = open("text_3.txt", "r", encoding="utf-8")
except IOError:
    print("Такого файла не существует")
else:
    salary_sum = 0
    employers = []
    for line in f:
        line = line.split()
        salary = float(line[1])
        salary_sum += salary
        if salary < 20000:
            employers.append(line[0])
    f.seek(0)
    print(f"Средняя зарплата: {salary_sum / len(f.readlines())}")
    print("Оклад менее 20000 имеют сотрудники: ", end="")
    for name in employers:
        print(name + " ", end="")
    f.close()
