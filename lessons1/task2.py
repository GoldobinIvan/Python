# 2. Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.

seconds = int(input("Вводите время в секундах "))
minutes = 0
hour = 0
while seconds > 59:
    seconds = seconds - 60
    minutes += 1
    if minutes > 59:
        hour += 1

print(f"{hour:02d}:{minutes:02d}:{seconds:02d}")
