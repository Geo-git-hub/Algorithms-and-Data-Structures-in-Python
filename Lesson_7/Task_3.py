"""

Массив размером 2m + 1, где m – натуральное число, заполнен случайным образом. Найдите
в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части: в
одной находятся элементы, которые не меньше медианы, в другой – не больше медианы.
Задачу можно решить без сортировки исходного массива. Но если это слишком сложно, то
используйте метод сортировки, который не рассматривался на уроках.
"""
import random
import statistics

m = random.randint(0, 10)
size = 2 * m + 1
dict_count_el = {}

lst = [random.randint(0, 100) for i in range(size)]
print(lst)

# проверка если длина входного списка 1
if len(lst) == 1:
    print(f'Медианой списка будет елемент {lst[0]}')
    exit(0)

result = None
distance = len(lst)

for el in lst:
    count_min = len(list([i for i in lst if i <= el]))
    if 0 < (count_min - m) < distance:
        distance = count_min - m
        result = el

print(f'Медианой списка будет елемент {result}')

"""
Онотация по количеству итерации O(n^2)
Онотация по памяти O(n)
если взять алгоритм с использованием сортировки, то будет продуктивнее предложенного выше алгоритма 
"""

#----Check---------------------------

print(f'Check = {statistics.median(lst)}')

print(statistics.median(lst) == result)
