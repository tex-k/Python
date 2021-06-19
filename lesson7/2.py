from abc import ABC, abstractmethod


class Clothes(ABC):
    @abstractmethod
    def consumption(self):
        pass


class Coat(Clothes):
    def __init__(self, v):
        self.__v = v

    @property
    def v(self):
        return self.__v

    def consumption(self):
        return self.__v / 6.5 + 0.5


class Suit(Clothes):
    def __init__(self, h):
        self.__h = h

    @property
    def h(self):
        return self.__h

    def consumption(self):
        return self.__h * 2 + 0.3


coat = Coat(2)
suit = Suit(2)

print(coat.v)
print(suit.h)
print(coat.consumption())
print(suit.consumption())
