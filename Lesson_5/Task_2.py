"""
Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое
число представляется как коллекция, элементы которой это цифры числа.
Например, пользователь ввёл A2 и C4F. Сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].
"""


class Hex_num:
    def __init__(self, number):
        self.number = list([el for el in number])

    def __int__(self):
        int_num = int(''.join(self.number), 16)
        return int_num

    def __add__(self, other):
        one = Hex_num.__int__(self)
        two = Hex_num.__int__(other)
        hex_sum = hex(int(one) + int(two))
        return Hex_num(hex_sum[2:])

    def __mul__(self, other):
        one = Hex_num.__int__(self)
        two = Hex_num.__int__(other)
        hex_mul = hex(int(one) * int(two))
        return Hex_num(hex_mul[2:])

    def __str__(self):
        return str(self.number).upper()


a = Hex_num(input(f'Введите первое число: '))
b = Hex_num(input(f'Введите второе число: '))
print(int(a))
print(f'Сумма чисел равна: {a + b}')
print(f'Произведение чисел равно: {a * b}')
