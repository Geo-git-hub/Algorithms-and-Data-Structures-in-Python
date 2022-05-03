"""
Посчитать четные и нечетные цифры введенного натурального числа.
Например, если введено число 34560, то у него 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
"""

while not (user_num := input(f'Укажите исходное число: ')).isdecimal():
    print(f'Вы указали некорректное число. Пример 24395')

even_number = 0
odd_number = 0
for el in user_num:
    el = int(el)
    if el % 2:
        odd_number += 1
    else:
        even_number += 1

print(f'В введённом числк {user_num} чётных цифр {even_number}, нечётных цифр {odd_number}')
