'''2. Создайте собственный класс-исключение,
обрабатывающий ситуацию деления на нуль.
Проверьте его работу на данных, вводимых пользователем.
При вводе пользователем нуля в качестве делителя программа
должна корректно обработать эту ситуацию и не завершиться с ошибкой.'''

class MyError(Exception):
    def __init__(self, txt):
        self.txt = txt

def div():
    while input('Для старта нажмите 1') == "1":
        try:
            divisible = int(input('Введите делимое'))
            divisor = int(input('Введите делитель'))
            if divisor == 0:
                raise MyError('Деление на 0 не возможно')
            else:
                res = divisible/divisor
                return res
        except ValueError:
            return "Вы ввели не число"
        except MyError as err:
            return err


print(div())