# 3. Реализовать функцию my_func(),
# которая принимает три позиционных аргумента,
# и возвращает сумму наибольших двух аргументов.

def my_func(argum_1, argum_2, argum_3):
    if argum_1 > argum_2:
        if argum_2 > argum_3:
            return argum_1 + argum_2
        elif argum_2 < argum_3:
            return argum_1 + argum_3
        else:
            print("Значения 2 и 3 равны")
            if argum_1 > argum_3:
                return argum_1 + argum_2
            elif argum_1 < argum_3:
                return argum_1 + argum_3
    elif argum_1 < argum_2:
        if argum_2 > argum_3:
            if argum_1 > argum_3:
                return argum_1 + argum_2
            elif argum_1 < argum_3:
                return argum_2 + argum_3
            else:
                return print("Значения 1 и 3 равны.")
        elif argum_2 < argum_3:
            return argum_2 + argum_3
        else:
            print("Значения 2 и 3 равны")
            if argum_1 > argum_3:
                return argum_1 + argum_2
            elif argum_1 < argum_3:
                return argum_1 + argum_3
    else:
        print("Значения 1 и 2 равны")
        if argum_1 > argum_3:
            return argum_1 + argum_2
        elif argum_1 < argum_3:
            return argum_1 + argum_3


str = input("Через пробел ввести три значения ")
while str != "!":
    arguments = str.split(" ")
    print(my_func(int(arguments[0]), int(arguments[1]), int(arguments[2])))
    str = input("Для остановления введите '!' ")