class Stationary:

    def __init__(self, title):
        self.__title = title

    def draw(self):
        print("Запуск отрисовки")

    def get_title(self):
        return self.__title


class Pen(Stationary):

    def draw(self):
        print("Запуск отрисовки ручкой")


class Pencil(Stationary):

    def draw(self):
        print("Запуск отрисовки карандашом")


class Handle(Stationary):

    def draw(self):
        print("Запуск отрисовки маркером")


stationary = Stationary("Канцелярская принадлежность")
pen = Pen("Ручка")
pencil = Pencil("Карандаш")
handle = Handle("Маркер")

print(stationary.get_title())
print(pen.get_title())
print(pencil.get_title())
print(handle.get_title())

stationary.draw()
pen.draw()
pencil.draw()
handle.draw()
