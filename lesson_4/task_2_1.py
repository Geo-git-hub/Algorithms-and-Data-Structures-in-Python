"""

Написать два алгоритма нахождения i-го по счёту простого числа.
"""

# Без использования «Решета Эратосфена»
# Представленный способ самый медленный по времени и самый многочисленный по количеству итераций
# на мой взгляд это O(n^2) квадратичная

import time

result = []
user_input = int(input(f'Введите икомое количество простых чисел: '))
i = 2
time_start = time.time()
while len(result) < user_input:
    flag = True
    for j in range(2, i):
        if not i % j:
            flag = False
            break
    if flag:
        result.append(i)

    i += 1
time_fin = time.time()

print(result)
print(time_fin - time_start, 'c')

print(len(result))

