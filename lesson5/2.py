try:
    f = open("text_1.txt", "r", encoding="utf-8")
except IOError:
    print("Такого файла не существует")
else:
    lines = f.readlines()

    line_amount = len(lines)
    print(f"Строк в файле: {line_amount}")

    for i in range(line_amount):
        print(f"Слов в строке {i + 1}: {len(lines[i].split())}")
    f.close()