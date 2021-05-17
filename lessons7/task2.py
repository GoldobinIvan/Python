'''2. Реализовать проект расчета суммарного расхода ткани на производство одежды.
Основная сущность (класс) этого проекта — одежда,
которая может иметь определенное название.
К типам одежды в этом проекте относятся пальто и костюм.
У этих типов одежды существуют параметры: размер (для пальто)
и рост (для костюма). Это могут быть обычные числа: V и H, соответственно.
Для определения расхода ткани по каждому типу одежды использовать
формулы: для пальто (V/6.5 + 0.5), для костюма (2 * H + 0.3).
Проверить работу этих методов на реальных данных.
Реализовать общий подсчет расхода ткани.
Проверить на практике полученные на этом уроке знания:
реализовать абстрактные классы для основных классов проекта,
проверить на практике работу декоратора @property.'''
from abc import ABC, abstractmethod


class Clothes(ABC):

    def __init__(self, param):
        self.param = param

    @abstractmethod
    def feature(self):
        pass

    @property
    def feature_suit(self):
        pass


class Coat(Clothes):
    def feature(self):
        return f"Для пошива пальто нужно {self.param / 6.5 + 0.5 :.2f} ткани"

    def feature_suit(self):
        return f"Для пошива пальто нужно {self.param / 6.5 + 0.5 :.2f} ткани"


class Suit(Clothes):
    def feature(self):
        return f"Для пошива костюма нужно {2 * self.param + 0.3} ткани"

    def feature_suit(self):
        return f"Для пошива костюма нужно {2 * self.param + 0.3} ткани"


coat = Coat(400)
suit = Suit(55)
print(coat.feature())
print(suit.feature())
print(coat.feature_suit())
print(suit.feature_suit())
