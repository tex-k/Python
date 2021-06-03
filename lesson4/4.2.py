lst = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]

new_lst = []
repeated_lst = []
[new_lst.append(el) if el not in new_lst and el not in repeated_lst else (repeated_lst.append(el), new_lst.remove(el) if el in new_lst else None) for el in lst]

print(new_lst)