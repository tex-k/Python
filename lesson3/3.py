def f(n1, n2, n3):
    n_list = [n1, n2, n3]
    n_list.remove(min(n_list))
    return sum(n_list)


print(f(2, 1, 5))