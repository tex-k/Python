time_sec = int(input("Введите время в секундах: "))

minutes = time_sec // 60
seconds = time_sec % 60
hours = minutes // 60
minutes = minutes % 60

print(f"{hours:02d}:{minutes:02d}:{seconds:02d}")
