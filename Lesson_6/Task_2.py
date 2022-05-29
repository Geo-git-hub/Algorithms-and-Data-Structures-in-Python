"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.


"""


"""
Пользователь вводит номер буквы в алфавите. Определить,
какая это буква.


В приведённом ниже примере:
 - временная сложность ( измеряяемая по количеству итераций) Онотация = O(1)
 - пространственная сложность - О(1)


"""

import sys

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z'
           ]
total_size = 0


def get_char_index(user_num):
    global total_size

    if not user_num.isdigit():
        raise ValueError('некорректно введён номер буквы')

    total_size += sys.getsizeof(user_num)

    user_num = int(user_num) - 1
    if user_num > len(alfabet) or user_num < 0:
        raise IndexError('число за пределами значения')

    return print(alfabet[user_num])


get_char_index(input(f'Введите индекс буквы: '))

total_size += sys.getsizeof(alfabet)
print("выделено памяти", total_size)


