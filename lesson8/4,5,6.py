class ImpossiblePrice(Exception):
    def __init__(self):
        self.text = "Невозможная цена"


class ImpossibleMemory(Exception):
    def __init__(self):
        self.text = "Невозможная величина памяти"


class ImpossibleDisplay(Exception):
    def __init__(self):
        self.text = "Невозможный тип дисплея"


class ImpossibleScArea(Exception):
    def __init__(self):
        self.text = "Невозможная область сканирования"


class Storage:
    def __init__(self):
        self.__equipments = {}
        self.__equipments_trans = {}

    def reception(self, equip):
        eq_list = self.__equipments.get(equip.get_type(), [])
        eq_list.append(equip)
        self.__equipments[equip.get_type()] = eq_list

    def transfer(self, equip, department):
        eq_list = self.__equipments_trans.get(equip.get_type(), [])
        eq_list.append((equip, department))
        self.__equipments_trans[equip.get_type()] = eq_list
        self.__equipments[equip.get_type()].remove(equip)

    @property
    def equipments(self):
        return self.__equipments

    @property
    def equipments_trans(self):
        return self.__equipments_trans


class Equipment:
    def __init__(self, brand, price):
        self.__brand = brand
        self.__price = Equipment.__valid_price(price)

    @classmethod
    def get_type(cls):
        return cls.__name__

    @staticmethod
    def __valid_price(value):
        try:
            value = float(value)
        except ValueError:
            raise ImpossiblePrice
        else:
            if value < 0:
                raise ImpossiblePrice
            else:
                return value

    @property
    def brand(self):
        return self.__brand

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, value):
        self.__price = Equipment.__valid_price(value)


class Printer(Equipment):
    def __init__(self, brand, price, memory):
        super().__init__(brand, price)
        self.__memory = Printer.__valid_memory(memory)

    @staticmethod
    def __valid_memory(value):
        try:
            value = int(value)
        except ValueError:
            raise ImpossibleMemory
        else:
            if value < 0:
                raise ImpossibleMemory
            else:
                return value

    @property
    def memory(self):
        return self.__memory


class Copier(Equipment):
    def __init__(self, brand, price, display):
        super().__init__(brand, price)
        self.__display = Copier.__valid_display(display)

    @staticmethod
    def __valid_display(value):
        if value == "colored" or value == "black_and_white":
            return value
        else:
            raise ImpossibleDisplay

    @property
    def display(self):
        return self.__display


class Scanner(Equipment):
    def __init__(self, brand, price, scanning_area):
        super().__init__(brand, price)
        self.__scanning_area = Scanner.__valid_sc_area(scanning_area)

    @staticmethod
    def __valid_sc_area(value):
        if "*" in value:
            value_list = value.split("*")
            try:
                v1 = int(value_list[0])
                v2 = int(value_list[1])
            except ValueError:
                raise ImpossibleScArea
            else:
                if v1 > 0 and v2 > 0:
                    return value

        raise ImpossibleScArea

    @property
    def scanning_area(self):
        return self.__scanning_area


storage = Storage()
printer_1 = Printer("HP", 2000, 64)
printer_2 = Printer("Canon", 1500, 64)
xerox = Copier("Xerox", 3000, "colored")
scanner = Scanner("Canon", 1000, "216*297")

storage.reception(printer_1)
storage.reception(printer_2)
storage.reception(xerox)
storage.reception(scanner)

print(storage.equipments)
print(storage.equipments["Printer"][0].brand)
print(storage.equipments["Printer"][1].brand)

storage.transfer(printer_1, "Отдел кадров")
storage.transfer(printer_2, "Юридический отдел")

print(storage.equipments)
print(storage.equipments_trans)
print(storage.equipments_trans["Printer"][0][0].brand)
print(storage.equipments_trans["Printer"][1][0].brand)
