# 7. Создать (не программно) текстовый файл,
# в котором каждая строка должна содержать
# данные о фирме: название, форма собственности,
# выручка, издержки.
# Необходимо построчно прочитать файл,
# вычислить прибыль каждой компании,
# а также среднюю прибыль.
# Если фирма получила убытки, в расчет средней
# прибыли ее не включать.
# Далее реализовать список.
# Он должен содержать словарь с фирмами и
# их прибылями, а также словарь со средней прибылью.
# Если фирма получила убытки, также добавить ее в словарь
# (со значением убытков).
import json

res = dict()
aver_profit = 0
num = 0
with open('text_7.txt', 'r', encoding='utf-8') as f:
    for line in f:
        name, type, income, cost = line.split()
        profit = int(income) - int(cost)
        if profit > 0:
            aver_profit += profit
            num += 1
        res[name] = profit
aver_profit /= num
with open('json7.json', 'w', encoding='utf-8') as f:
    json.dump([res, {"average_profit": aver_profit}], f, ensure_ascii=False)