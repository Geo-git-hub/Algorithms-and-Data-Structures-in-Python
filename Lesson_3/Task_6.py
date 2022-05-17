"""
В одномерном массиве найти сумму элементов,
находящихся между минимальным и максимальным элементами.
Сами минимальный и максимальный элементы в сумму не включать.
"""

from random import randint

init_random_list = [randint(1, 100) for el in range(29 + 1)]
print(init_random_list)

min_index = init_random_list.index(min(init_random_list))
max_index = init_random_list.index(max(init_random_list))

print(f'позиции мин и мак элементов {min_index, max_index}')

if min_index - max_index not in (-1, 1):
    result = init_random_list[min(min_index, max_index) + 1: max(min_index, max_index)]
    print(*result)
    print(f' Сумма чисел = {sum(result)}')
else:
    print(f'между позициями нет элементов {min_index, max_index}')