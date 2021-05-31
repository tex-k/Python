my_list = [7, 5, 3, 3, 2]

while True:
    try:
        n = int(input("Введите число: "))
        break
    except ValueError:
        print("Необходимо ввести число")

flag = 0

for i, item in enumerate(my_list):
    if n > item:
        my_list.insert(i, n)
        flag = 1
        break

if not flag:
    my_list.append(n)

print(my_list)
