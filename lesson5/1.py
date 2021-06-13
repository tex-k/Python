with open("text_1.txt", "w", encoding="utf-8") as f:
    while True:
        line = input("Введите строку: ")
        if line == "":
            break
        f.write(line + "\n")
