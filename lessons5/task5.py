# 5. Создать (программно) текстовый файл,
# записать в него программно набор чисел,
# разделенных пробелами.
# Программа должна подсчитывать сумму
# чисел в файле и выводить ее на экран.

from random import randint

with open("text_5.txt", "w", encoding="utf-8") as f:
    my_list = [randint(1, 100) for _ in range(100)]
    f.write(" ".join(map(str, my_list)))

print(f"Сумма чисел - {sum(my_list)}")