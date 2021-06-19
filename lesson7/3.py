class Cell:
    def __init__(self, amount):
        self.__amount = amount

    def __add__(self, other):
        return Cell(self.amount + other.amount)

    def __sub__(self, other):
        sub = self.amount - other.amount
        if sub > 0:
            return Cell(sub)
        else:
            print("Невозможная операция")
            return Cell(0)

    def __mul__(self, other):
        return Cell(self.amount * other.amount)

    def __truediv__(self, other):
        return Cell(self.amount // other.amount)

    def make_order(self, row):
        s = ""
        for i in range(self.amount // row):
            for j in range(row):
                s += "*"
            s += "\n"
        for i in range(self.amount % row):
            s += "*"
        return s

    @property
    def amount(self):
        if self.__amount:
            return self.__amount


cell_1 = Cell(12)
cell_2 = Cell(15)

print((cell_1 + cell_2).amount)
print((cell_1 - cell_2).amount)
print((cell_2 - cell_1).amount)
print((cell_1 * cell_2).amount)
print((cell_1 / cell_2).amount)
print((cell_2 / cell_1).amount)
print(cell_1.make_order(5))
print(cell_2.make_order(5))
