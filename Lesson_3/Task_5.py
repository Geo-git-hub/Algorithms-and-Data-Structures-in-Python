"""

В массиве найти максимальный отрицательный элемент. Вывести на экран его значение и позицию в массиве.
"""

from random import randint

init_random_list = [randint(-100, -1) for el in range(20)]
print(init_random_list)

# print(sorted(init_random_list)) # для наглядности

max_el = max(init_random_list)
max_index = init_random_list.index(max_el)

print(f'Макс элемент {max_el} на {max_index + 1} позиции')