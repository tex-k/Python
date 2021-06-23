class Date:
    def __init__(self, date_str):
        Date.parse(date_str)

    @classmethod
    def parse(cls, date_str):
        date_list = date_str.split("-")
        date_tuple = cls.__validate(int(date_list[0]), int(date_list[1]), int(date_list[2]))
        cls.day = date_tuple[0]
        cls.month = date_tuple[1]
        cls.year = date_tuple[2]

    @staticmethod
    def __validate(day, month, year):
        right_day = None
        right_month = None
        right_year = None

        if 1 <= day <= 31:
            right_day = day

        if 1 <= month <= 12:
            right_month = month

        if year > 0:
            right_year = year

        return right_day, right_month, right_year


date = Date("01-02-2000")

print(date.day, date.month, date.year)
