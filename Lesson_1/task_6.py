"""
Пользователь вводит номер буквы в алфавите. Определить,
какая это буква.

"""

alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z'
           ]


def get_char_index(user_num):
    if not user_num.isdigit():
        raise ValueError('некорректно введён номер буквы')

    user_num = int(user_num) - 1
    if user_num > len(alfabet) or user_num < 0:
        raise IndexError('число за пределами значения')

    return print(alfabet[user_num])


get_char_index(input(f'Введите индекс буквы: '))
