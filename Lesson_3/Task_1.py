"""
В диапазоне натуральных чисел от 2 до 99 определить, сколько из них кратны каждому из чисел в диапазоне от 2 до 9.
"""
num_end = 100
denominator = [el for el in range(2, 10)]


def check_denominator(num):
    for el in denominator:
        if num % el:
            return False
    return True


numbers = [num for num in range(2, num_end) if check_denominator(num)]
if len(numbers) == 0:
    print('В указанном диапазоне нет чисел кратных каждому из (2:9)')
else:
    print(len(numbers))
    print(numbers)

# ==================  способ 2 ==========================
k = 0
for i in range(2, num_end):
    for x in range(2, 10):
        if i % x:
            break

    else:
        k += 1
        print(i, end=";")

print(f'\n в диапазоне {k} чисел ')