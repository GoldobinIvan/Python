# 6. Реализовать два небольших скрипта:
# а) итератор, генерирующий целые числа, начиная с указанного,
# б) итератор, повторяющий элементы некоторого списка, определенного заранее.

from itertools import islice, cycle, count


def iterator_integers(start, stop, step):
    if start.isnumeric() and stop.isnumeric() and step.isnumeric():
        start, stop, step = int(start), int(stop), int(step)
        new_list = [el for el in islice(count(), int(start), int(stop + 1), int(step))]
        return new_list
    else:
        print("Ошибка")


print(iterator_integers(input("Первое значение "), input("Последнее значение "), input("Шаг ")))

