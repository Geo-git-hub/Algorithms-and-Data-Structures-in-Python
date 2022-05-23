"""
Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4
квартала (т.е. 4 отдельных числа) для каждого предприятия.. Программа должна определить
среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий, чья
прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже
среднего.
"""
import collections

company_count = int(input(f'Укажите количество компаний: '))

dict_company = collections.defaultdict(list)

for i in range(1, company_count + 1):
    c_name = input(f'Укажите название {i} фирмы: ')
    # dict_company[c_name] = []
    for month in range(1, 5):
        profit = float(input(f'Укажите прибыль за {month} месяц: '))
        dict_company[c_name].append(profit)


for el in dict_company.items():
    print(el)

global_profit = 0
for el in dict_company.values():
    global_profit += sum(el)

avrg_profit = global_profit / company_count
print(f' средняя: {avrg_profit}')

copm_compare_avrg = {'above_average': [], 'less_average': []}


for el in dict_company:
    if sum(dict_company[el]) > avrg_profit:
        copm_compare_avrg['above_average'].append(el)
    elif sum(dict_company[el]) < avrg_profit:
        copm_compare_avrg['less_average'].append(el)

print(f"Список компании с прибылью выше среднего значения: {copm_compare_avrg['above_average']}")
print(f"Список компании с прибылью ниже среднего значения: {copm_compare_avrg['less_average']}")