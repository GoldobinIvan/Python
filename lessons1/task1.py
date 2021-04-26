name = input("Введите Ваше имя ")
print("Привет,", name)
print("Давай сыграем я загадываю число от 1 до 9")
number = int(input("Твой вариант"))
meaning = 5
while meaning != number:
    print("Неверено, попробуй еще раз")
    number = int(input("Твой вариант "))
print("Угадал,", name)