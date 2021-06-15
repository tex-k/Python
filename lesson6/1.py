import time


class TrafficLight:

    __color = ["Красный", "Жёлтый", "Зелёный"]

    def running(self):
        for i in range(3):
            print(self.__color[i])
            if i == 0:
                time.sleep(7)
            else:
                time.sleep(2)


tl = TrafficLight()
tl.running()
