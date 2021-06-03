from functools import reduce


def f(n1, n2):
    return n1 * n2


print(reduce(f, [el for el in range(100, 1001) if el % 2 == 0]))
