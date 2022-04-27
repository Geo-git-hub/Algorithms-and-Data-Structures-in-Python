"""
Написать программу, которая генерирует в указанных пользователем границах:

случайное целое число;
случайное вещественное число;
случайный символ.

Для каждого из трех случаев пользователь задает свои границы диапазона.
Например, если надо получить случайный символ от 'a' до 'f', то вводятся эти символы.
Программа должна вывести на экран любой символ алфавита от 'a' до 'f' включительно.

"""
import random


def generate_int_number(start_number, end_number):
    if not start_number.isdigit() or not end_number.isdigit():
        raise Exception('некорректный ввод')

    start_number = int(start_number)
    end_number = int(end_number)

    if end_number < start_number:
        raise Exception('некорректный ввод конечного числа')

    return print(random.randint(start_number, end_number))


def generate_float_number(start_number, end_number):
    try:
        start_number = float(start_number)
        end_number = float(end_number)
    except ValueError:
        return print('Некорректный ввод числа')


    if end_number < start_number:
        raise Exception('Некорректный ввод конечного числа')

    return print((end_number - start_number) * random.random() + start_number)


alfabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z'
           ]


def get_char(start_chr, end_chr):
    if not start_chr.isalpha() or not end_chr.isalpha():
        raise Exception('некорректный ввод')

    try:
        start_chr = alfabet.index(start_chr.lower())
        end_chr = alfabet.index(end_chr.lower())
    except ValueError:
        return print('некорректный ввод')

    answer_chr = random.randint(start_chr, end_chr)

    return print(alfabet[answer_chr])


print(f'для генерации случайного целого числа \n ')
generate_int_number(input('укажите начало интервала: '), input('укажите конец интервала: '))

print(f'для генерации случайного вещественного числа \n ')
generate_float_number(input('укажите начало интервала: '), input('укажите конец интервала: '))

print(f'для генерации случайного символа из английского языка \n ')
get_char(input('укажите начальный символ: '), input('укажите конечный символ: '))
