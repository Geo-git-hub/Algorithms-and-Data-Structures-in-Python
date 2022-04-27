"""
Пользователь вводит две буквы. Определить их порядковый
номер в алфавите и рассчитать число букв между ними

"""
alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z'
           ]


def get_char_info(start_char, end_char):
    if not start_char.isalpha() or not end_char.isalpha():
        raise ValueError('некорректный ввод, это не буквы')

    try:
        start_num = alfabet.index(start_char.lower()) + 1
        end_num = alfabet.index(end_char.lower()) + 1
    except ValueError:
        return print('некорректный ввод, введите маленькие буквы из английского алфавита')

    return print(f'У введённого символа "{start_char}" порядковый номер {start_num} \n',
                 f'У введённого символа "{end_char}" порядковый номер {end_num} \n',
                 f' количество символов между ними {end_num - start_num}'
                 )


get_char_info(input('укажите начальный символ: '), input('укажите конечный символ: '))
