"""
Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
Проанализировать результат и определить программы с наиболее эффективным использованием памяти.

"""

"""

Определить, является ли год, который ввел пользователем, високосным или невисокосным.

временная сложность O(1)
пространственная сложность O(1)


"""
import sys

user_year = input(f'Введите год : ')
print(f"выделено памяти под переменные: {sys.getsizeof(user_year)}")
try:
    user_year = int(user_year)
    if user_year % 4 == 0 and user_year % 100 and user_year % 400:
        print(f'{user_year} високосный.')
    else:
        print(f'{user_year} не високосный.')
except ValueError:
    print(f'Некорректный ввод')