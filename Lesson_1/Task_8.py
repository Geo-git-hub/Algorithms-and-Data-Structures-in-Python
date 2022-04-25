"""

Определить, является ли год, который ввел пользователем, високосным или невисокосным.

"""

user_year = input(f'Введите год : ')
try:
    user_year = int(user_year)
    if user_year % 4 == 0 and user_year % 100 and user_year % 400:
        print(f'{user_year} високосный.')
    else:
        print(f'{user_year} не високосный.')
except ValueError:
    print(f'Некорректный ввод')