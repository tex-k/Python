class Car:

    def __init__(self, speed, color, name):
        self.__speed = speed
        self.__color = color
        self.__name = name
        self.__is_police = False

    def go(self):
        print("Машина поехала")

    def stop(self):
        print("Машина остановилась")

    def turn(direction):
        print(f"Машина повернула на{direction}")

    def set_police(self):
        self.__is_police = True

    def get_speed(self):
        return self.__speed

    def show_speed(self):
        print(self.__speed)


class TownCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.get_speed() > 60:
            print("Скорость превышена")


class SportCar(Car):
    pass


class WorkCar(Car):

    def show_speed(self):
        super().show_speed()
        if self.get_speed() > 40:
            print("Скорость превышена")


class PoliceCar(Car):

    def __init__(self, speed, color, name):
        super().__init__(speed, color, name)
        self.set_police()


tc = TownCar(70, "жёлтый", "Mazda")
sc = SportCar(120, "серебристый", "Porshe")
wc = WorkCar(50, "зелёный", "Lada")
pc = PoliceCar(30, "фиолетовый", "Запорожец")

tc.show_speed()
sc.show_speed()
wc.show_speed()
pc.show_speed()

print(vars(tc))
print(vars(sc))
print(vars(wc))
print(vars(pc))
