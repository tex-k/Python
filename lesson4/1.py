from sys import argv


def f(hours, salary, premium):
    return hours * salary + premium


print(f(float(argv[1]), float(argv[2]), float(argv[3])))