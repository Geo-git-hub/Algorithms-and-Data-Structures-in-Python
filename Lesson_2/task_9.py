"""
Среди натуральных чисел, которые были введены, найти наибольшее по сумме цифр.
Вывести на экран это число и сумму его цифр.
"""
counter = 1
max_sum_number = "0"


def get_sum(complex_num):
    subtotal = 0
    for el in complex_num:
        subtotal += int(el)

    return subtotal


while (user_input := input(f'Введите {counter} число, для завершения введите пустую строку: ')) != '':
    counter += 1

    if not user_input.isdecimal():
        continue

    if get_sum(user_input) > get_sum(max_sum_number):
        max_sum_number = user_input

print(f'Наибольшее по сумме цифр {max_sum_number}')
