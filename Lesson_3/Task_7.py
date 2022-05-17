"""
В одномерном массиве целых чисел определить два наименьших элемента.
Они могут быть как равны между собой (оба являться минимальными), так и различаться.
"""

from random import randint

init_random_list = [randint(1, 100) for el in range(29 + 1)]
print(init_random_list)

init_random_list.sort()
print(init_random_list)
print(f'минимальные элементы массива: {init_random_list[:2]}')