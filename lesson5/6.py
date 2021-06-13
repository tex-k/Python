lessons = {}

try:
    f = open("text_6.txt", "r", encoding="utf-8")
except IOError:
    print("Файла не существует")
else:
    for line in f:
        line_list = line.split()
        name = line_list[0][:-1]
        summa = 0
        if line_list[1] != "-":
            summa += int(line_list[1][:-3])
        if line_list[2] != "-":
            summa += int(line_list[2][:-4])
        if line_list[3] != "-":
            summa += int(line_list[3][:-5])
        lessons[name] = summa
    f.close()

print(lessons)
