class ZeroDenominator(Exception):
    def __init__(self):
        self.text = "Нулевой знаменатель"


try:
    denominator = int(input("Введите знаменатель: "))
    if denominator == 0:
        raise ZeroDenominator
except ZeroDenominator as e:
    print(e.text)
else:
    print(denominator)
