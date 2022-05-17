"""
Найти максимальный элемент среди минимальных элементов столбцов матрицы
"""
from random import randint

matrix = []

for i in range(5):
    line = [randint(1, 99) for el in range(10)]
    matrix.append(line)

for line in matrix:
    for el in line:
        print(f'{el:02}', end=' ')
    print()

print('== ' * 10)

columns_count = len(matrix[0])
list_min_el = []

for j in range(columns_count):
    min_col_el = min([matrix[i][j] for i in range(len(matrix))])
    print(f'{min_col_el:02}', end=' ')
    list_min_el.append(min_col_el)

print(f'\nмаксимальный из минимальных в столбце: {max(list_min_el)}')