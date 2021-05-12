# 4. Создать (не программно) текстовый файл
# со следующим содержимым:
# One — 1
# Two — 2
# Three — 3
# Four — 4
# Необходимо написать программу,
# открывающую файл на чтение и
# считывающую построчно данные.
# При этом английские числительные
# должны заменяться на русские.
# Новый блок строк должен
# записываться в новый текстовый файл.


with open("text_4.txt", 'r') as f, open('text_4.txt', 'w', encoding="utf-8") as fil:
    numb_dict = {'One': 'Один', 'Two': 'Два', 'Three': 'Три', 'Four': 'Четыре'}
    my_str = str()
    for line in f:
        line = line.split()
        for item in numb_dict.items():
            if line[0] == item[0]:
                line[0] = item[1]
                my_str = " ".join(line)
                fil.writelines(my_str + '\n')
