class ComplexNumber:
    def __init__(self, re, im):
        self.__re = re
        self.__im = im

    def __str__(self):
        return f"{self.__re} {'-' if self.im < 0 else '+'} i * {self.im if self.im > 0 else -self.im}"

    def __add__(self, other):
        return ComplexNumber(self.re + other.re, self.im + other.im)

    def __mul__(self, other):
        return ComplexNumber(self.re * other.re - self.im * other.im, self.re * other.im + self.im * other.re)

    @property
    def re(self):
        return self.__re

    @property
    def im(self):
        return self.__im


n1 = ComplexNumber(5, 6)
n2 = ComplexNumber(2, -1)
print(n1)
print(n2)
print(n1 + n2)
print(n1 * n2)
