"""
В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.

"""

from random import randint

init_random_list = [randint(1, 1000) for el in range(20)]
print(init_random_list)
# print(f'проверка мин и макс значений  {sorted(init_random_list)}')

min_num, max_num = min(init_random_list), max(init_random_list)
min_index, max_index = init_random_list.index(min_num), init_random_list.index(max_num)

init_random_list[min_index] = max_num
init_random_list[max_index] = min_num



print(init_random_list)