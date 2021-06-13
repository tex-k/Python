trans_dict = {"one": "один", "two": "два", "three": "три", "four": "четыре"}

try:
    f = open("text_4.txt", "r", encoding="utf-8")
except IOError:
    print("Файла не существует")
else:
    with open("text_4_new.txt", "w", encoding="utf-8") as f_new:
        for line in f:
            line_list = line.split()
            line_list.insert(0, trans_dict[line_list.pop(0).lower()].capitalize())
            f_new.write(" ".join(line_list) + "\n")
    f.close()