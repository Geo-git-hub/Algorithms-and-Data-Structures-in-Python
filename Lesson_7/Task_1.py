"""
Отсортируйте по убыванию методом "пузырька" одномерный целочисленный массив,
заданный случайными числами на промежутке [-100; 100).
Выведите на экран исходный и отсортированный массивы.
Сортировка должна быть реализована в виде функции.
По возможности доработайте алгоритм (сделайте его умнее).

"""

"""
Онотация по количеству итерации О(n^2)
по памяти O(n)

"""
import random

len_matrix = 10

matrix = [random.randint(-100, 99) for i in range(len_matrix)]

print(f'Исходный массив \n{matrix}')


# matrix.sort() #тестил flag

def bubble_sort_min(lst, reverse=False):
    flag = False
    n = 1
    while n < len(lst):
        for i in range(len(lst) - n):
            if reverse:
                if lst[i] < lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    flag = True
            elif not reverse:
                if lst[i] > lst[i + 1]:
                    lst[i], lst[i + 1] = lst[i + 1], lst[i]
                    flag = True

        if flag:
            flag = False
        else:
            break

        n += 1

    return lst


matrix_sort = bubble_sort_min(matrix.copy(), reverse=True)
print(f'Отсортирован при помощи пузырька \n{matrix_sort}')

print('Контролька ')
matrix.sort(reverse=True)
print(matrix)
