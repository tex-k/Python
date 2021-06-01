def f(name, surname, birth_year, city, email, phone):
    return f"имя: {name}, фамилия: {surname}, год рождения: {birth_year}, город: {city}, email: {email}, телефон: {phone}"


name = input("Введите имя: ")
surname = input("Введите фамилию: ")
birth_year = input("Введите год рождения: ")
city = input("Введите город: ")
email = input("Введите email: ")
phone = input("Введите номер телефона: ")
print(f(name=name, surname=surname, birth_year=birth_year, city=city, email=email, phone=phone))
