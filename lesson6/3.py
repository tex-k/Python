class Worker:

    def __init__(self, name, surname, position, wage, bonus):
        self.name = name
        self.surname = surname
        self.position = position
        self.__income = {"wage": wage, "bonus": bonus}

    def get_income(self):
        return self.__income


class Position(Worker):

    def __init__(self, name, surname, position, wage, bonus):
        super().__init__(name, surname, position, wage, bonus)

    def get_full_name(self):
        return self.name + " " + self.surname

    def get_total_income(self):
        return self.get_income()["wage"] + self.get_income()["bonus"]


pos = Position("Иван", "Иванов", "слесарь", 30000, 5000)
print(vars(pos))
print(pos.get_full_name())
print(pos.get_total_income())