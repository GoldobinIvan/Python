# 4. Реализуйте базовый класс Car.
# У данного класса должны быть следующие
# атрибуты: speed, color, name, is_police (булево).
# А также методы: go, stop, turn(direction),
# которые должны сообщать, что машина поехала,
# остановилась, повернула (куда).
# Опишите несколько дочерних классов:
# TownCar, SportCar, WorkCar, PoliceCar.
# Добавьте в базовый класс метод show_speed,
# который должен показывать текущую скорость автомобиля.
# Для классов TownCar и WorkCar переопределите метод show_speed.
# При значении скорости свыше 60 (TownCar) и
# 40 (WorkCar) должно выводиться сообщение о превышении скорости.
# Создайте экземпляры классов, передайте значения атрибутов.
# Выполните доступ к атрибутам, выведите результат.
# Выполните вызов методов и также покажите результат.

class Car:
    def __init__(self, name, speed, color, is_police):
        self.speed = speed
        self.color = color
        self.name = name
        self.is_police = is_police

    def go(self):
        return f"{self.name} поехала"

    def stop(self):
        return f"{self.name} остановилась"

    def turn(self, direction):
        return f"{self.name} повернула {'направо' if direction == 0 else 'налево'}"

    def show_speed(self):
        return f"{self.name} двигается со скоростью {self.speed}"


class TownCar(Car):
    def show_speed(self):
        if int(self.speed) >= 60:
            return f"Скорость превышена"
        else:
            return f"Скорость в норме"


class SportCar(Car):
    pass


class WorkCar(Car):
    def show_speed(self):
        if int(self.speed) >= 40:
            return f"Скорость превышена"
        else:
            return f"Скорость в норме"


class PoliceCar(Car):
    pass


town = TownCar('Audi', 70, 'blue', False)
print('1:\n' + town.go(), town.show_speed(), town.turn(1), town.turn(2), town.stop())

sport = SportCar('AudiRS', 170, 'red', False)
print('2:\n' + sport.go(), sport.show_speed(), sport.turn(1), sport.stop())

work = WorkCar('WAZ', 30, 'red', False)
print('3:\n' + work.go(), work.show_speed(), work.turn(2), work.stop())

police = PoliceCar('Kia', 100, 'yellow', True)
print('4:\n' + work.go(), work.show_speed(), work.turn(2), work.stop())
