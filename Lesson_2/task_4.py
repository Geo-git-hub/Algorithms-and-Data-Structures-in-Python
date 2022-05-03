"""
Найти сумму n элементов следующего ряда чисел: 1 -0.5 0.25 -0.125 ...
Количество элементов (n) вводится с клавиатуры.
"""


def denominator(n):
    if n == 1:
        return 1
    return denominator(n - 1) * 2


number_elements = int(input(f'Укажите количество элементов: '))
sum_elements = 0

for el in range(1, number_elements + 1):
    if not el % 2:
        znak = -1
    else:
        znak = 1
    sum_elements += znak * (1 / denominator(el))

print(f'сумма {number_elements} элементов {sum_elements}')
