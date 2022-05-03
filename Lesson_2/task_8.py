"""
Посчитать, сколько раз встречается определенная цифра в введенной последовательности чисел.
Количество вводимых чисел и цифра, которую необходимо посчитать, задаются вводом с клавиатуры.
"""
user_list_number = input(f'Через запятую укажите последовательнось чисел: ')
user_list_number = user_list_number.replace(' ', '')
user_list_number = user_list_number.split(',')

user_searched_num = input(f'Введите искомое число: ')

print(f'Искомое число встречается {user_list_number.count(user_searched_num)} раз')