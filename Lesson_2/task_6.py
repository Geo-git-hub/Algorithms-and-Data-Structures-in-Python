"""
В программе генерируется случайное целое число от 0 до 100.
Пользователь должен его отгадать не более чем за 10 попыток.
После каждой неудачной попытки должно сообщаться больше или меньше введенное пользователем число,
чем то, что загадано. Если за 10 попыток число не отгадано, то вывести загаданное число.
"""
import random

hidden_num = random.randint(0, 100)

for attempt in range(1, 10 + 1):

    print(f'Попытка номер {attempt}')

    if not (user_input := input(f'Укажите целое число: ')).isdigit():
        print(f'Некорректный ввод, попытка зачтена')
        continue

    user_input = int(user_input)
    if user_input < hidden_num:
        print(f'Указанное число меньше загаданного')
    elif user_input > hidden_num:
        print(f'Указанное число больше загаданного')
    elif user_input == hidden_num:
        print(f'Вы угадали')
        break

print(f'Было загаданно число {hidden_num}')
