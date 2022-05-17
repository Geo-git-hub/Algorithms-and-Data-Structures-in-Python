"""
Матрица 5x4 заполняется вводом с клавиатуры кроме последних элементов строк.
Программа должна вычислять сумму введенных элементов каждой строки и
записывать ее в последнюю ячейку строки. В конце следует вывести полученную матрицу.
"""

matrix = []

for i in range(5):
    while True:
        user_input = input(f'для строки {i + 1} введите 3 числа через пробел: ')
        user_input = user_input.strip().split(" ")

        if len(user_input) != 3:
            print(f'Некорректный ввод!')
            continue
        else:
            break

    user_input = list(map(int, user_input))
    user_input.append(sum(user_input))
    matrix.append(user_input)

print('-----------result-----------')
for line in matrix:
    print(*line)
