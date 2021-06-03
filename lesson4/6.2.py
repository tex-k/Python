from itertools import cycle

lst = [1, 2, 3, 4, 5]

i = 0
for el in cycle(lst):
    i += 1
    print(el)
    if i == len(lst) * 5:
        break
