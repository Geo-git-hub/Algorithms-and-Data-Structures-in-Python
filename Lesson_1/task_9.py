"""

Вводятся три разных числа. Найти, какое из них является средним (больше одного, но меньше другого).

"""
numbers_list = []
for i in range(1, 4):
    while not (user_input := input(f'ВВедите {i}-е число: ')).isdigit():
        pass

    numbers_list.append(int(user_input))

# numbers_list.sort()
print(f'Из введённых {numbers_list}, среднее {sorted(numbers_list)[1]}')
