# 2. Реализовать функцию, принимающую несколько параметров, описывающих данные пользователя:
# имя, фамилия, год рождения, город проживания, email, телефон.
# Функция должна принимать параметры как именованные аргументы.
# Реализовать вывод данных о пользователе одной строкой.

def my_func(*args):
    return print(f"{name} {surname} {year_of_birth} {city_of_birth} {email} {phone}")


name = "Иван"
surname = "Иванов"
year_of_birth = "12.02.2000"
city_of_birth = "Москва"
email = "qwert@un.ru"
phone = "8(978)951-54-54"
my_func(name, surname, year_of_birth, city_of_birth, email, phone)