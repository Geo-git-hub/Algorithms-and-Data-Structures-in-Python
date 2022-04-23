"""
Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.

"""
from math import prod


def evaluate_sum_product(user_input):
    number_list = [int(el) for el in user_input]
    return print(f'Для введённого числа: {user_input}, сумма = {sum(number_list)}, произведение = {prod(number_list)}')


while (user_input := input('Введите трёхзначное число: ')) != '':
    if user_input.isdigit() and len(user_input) == 3:
        evaluate_sum_product(user_input)
        break
