class NotNumber(Exception):
    def __init__(self):
        self.text = "Не число"


def is_negative(number_str):
    if number_str[0] == "-":
        return True
    else:
        return False


def is_float(number_str):
    if "." in number_str:
        number_list = number_str.split(".")
        if len(number_list) == 2 and number_list[0].isdigit() and number_list[1].isdigit():
            return True

    return False


def is_number(number_str):
    if number_str.isdigit():
        return True
    elif is_negative(number_str) and number_str[1:].isdigit():
        return True
    elif is_float(number_str):
        return True
    elif is_negative(number_str) and is_float(number_str[1:]):
        return True
    else:
        return False


my_list = []
while True:
    try:
        number_str = input("Введите число (или ничего для остановки): ")
        if not number_str:
            break
        elif not is_number(number_str):
            raise NotNumber
    except NotNumber as e:
        print(e.text)
    else:
        my_list.append(number_str)

print(my_list)
