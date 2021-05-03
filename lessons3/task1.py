# 1. Реализовать функцию, принимающую два числа
# (позиционные аргументы) и выполняющую их деление.
# Числа запрашивать у пользователя,
# предусмотреть обработку ситуации деления на ноль.

def division(argum_1, argum_2):
    if argum_2 == 0:
        return print("Деление на ноль не возможно ")
    else:
        return argum_1 / argum_2


str = input("Через пробел ввести два значения, первый будет разделен на второй ")
while str != "!":
    arguments = str.split(" ")
    print(division(float(arguments[0]), float(arguments[1])))
    str = input("Для остановления введите '!' ")