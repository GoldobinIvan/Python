#4. Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.

number = int(input("Введите целое положительное число "))
meaning = -1
while (number % 10) > 0:
    if meaning < number % 10:
        meaning = number % 10
    print("цифра " + str(meaning))
    number = number // 10
    print("само число " + str(number))
print(meaning)