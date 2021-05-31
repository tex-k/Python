my_list = []

while True:
    item = input("Введите элемент или stop для остановки: ")
    if item == "stop":
        break
    my_list.append(item)

for i in range(len(my_list)):
    if (i % 2 == 0):
        continue
    my_list[i - 1], my_list[i] = my_list[i], my_list[i - 1]

print(my_list)
