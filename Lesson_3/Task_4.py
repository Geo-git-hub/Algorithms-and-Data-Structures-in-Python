"""
Определить, какое число в массиве встречается чаще всего.
"""
from random import randint

init_random_list = [randint(1, 1000) for el in range(20)]

init_random_list.sort()  # для наглядности
print(init_random_list)

el_count = {}

for el in init_random_list:
    if el not in el_count:
        el_count[el] = 1
    else:
        el_count[el] += 1

print(el_count)

max_val = max(el_count.values())
print(f'max {max_val}')
if max_val > 1:
    for key, val in el_count.items():
        if val == max_val:
            print(f'Число {key} встречается {val} раз ')
else:
    print(f'все элементы встречаются однократно')
