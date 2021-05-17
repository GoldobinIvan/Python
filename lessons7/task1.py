# 1. Реализовать класс Matrix (матрица).
# Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин,
# расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__()
# для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__()
# для реализации операции сложения двух объектов
# класса Matrix (двух матриц).
# Результатом сложения должна быть новая матрица.
# # Подсказка: сложение элементов матриц выполнять поэлементно —
# первый элемент первой строки первой матрицы складываем
# с первым элементом первой строки второй матрицы и т.д.
import random as r

import self as self


class Matrix:
    def __init__(self, matrix_list):
        self.matrix_list = matrix_list

    def __str__(self):
        for row in self.matrix_list:
            for i in row:
                print(f"{i:4}", end="")
            print()
        return ''


    def __add__(self, other):
        for i in range(len(self.matrix_list)):
            for i_2 in range(len(other.matrix_list[i])):
                self.matrix_list[i][i_2] = self.matrix_list[i][i_2] + other.matrix_list[i][i_2]
        return Matrix.__str__(self)


m = Matrix([[r.randint(-10, 10), r.randint(-10, 10), r.randint(-10, 10)], [r.randint(-10, 10), r.randint(-10, 10), r.randint(-10, 10)],
            [r.randint(-10, 10), r.randint(-10, 10), r.randint(-10, 10)], [r.randint(-10, 10), r.randint(-10, 10), r.randint(-10, 10)]])
new_m = Matrix([[r.randint(-10, 10), r.randint(-10, 10), r.randint(-10, 10)], [r.randint(-10, 10), r.randint(-10, 10), r.randint(-10, 10)],
            [r.randint(-10, 10), r.randint(-10, 10), r.randint(-10, 10)], [r.randint(-10, 10), r.randint(-10, 10), r.randint(-10, 10)]])
print(m.__str__())
print(new_m.__str__())
print(m.__add__(new_m))