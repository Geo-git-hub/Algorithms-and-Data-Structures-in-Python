"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

"""
from math import prod

while (user_input := input('Введите трёхзначное число(для завершения введите пустое значение): ')) != '':
    if user_input.isdigit() and len(user_input) == 3:
        number_list = [int(el) for el in user_input]
        print(f'Для введённого числа: {user_input}, сумма = {sum(number_list)}, произведение = {prod(number_list)}')
