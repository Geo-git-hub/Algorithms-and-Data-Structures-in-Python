"""
Напишите программу, доказывающую или проверяющую,
что для множества натуральных чисел выполняется равенство: 1+2+...+n = n(n+1)/2, где n - любое натуральное число.
"""

user_input = abs(int(input(f'Укажите число: ')))

simpl_sum = sum(range(1, user_input + 1))
complicate_sum = user_input * (user_input + 1) / 2

print(simpl_sum, " ", complicate_sum, simpl_sum == complicate_sum)
