#3. Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3.
# Считаем 3 + 33 + 333 = 369.

number = input("Введите число ")
number_two = number + number
number_three = number + number_two
print(number + "+" + number_two + "+" + number_three)
sum = int(number) + int(number_two) + int(number_three)
print(sum)
