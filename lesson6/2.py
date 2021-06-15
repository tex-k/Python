class Road:

    __depth = 5
    __unit_mass = 25

    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass(self):
        return self.__depth * self.__unit_mass * self.__length * self.__width / 1000


road = Road(5000, 20)
print(road.mass())