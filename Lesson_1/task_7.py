"""
По введенным пользователем длинам трех отрезков определить,
можно ли составить из этих отрезков треугольник. Если да,
определить, будет ли треугольник разносторонним,
равнобедренным или равносторонним.

"""


def check_triangle(side_1, side_2, side_3):
    triangle_sides = []

    try:
        triangle_sides.append(float(side_1))
        triangle_sides.append(float(side_2))
        triangle_sides.append(float(side_3))

    except ValueError:
        return print('Введите положительные числа больше 0')

    for side in triangle_sides:
        if side == 0:
            return print(f'Введите положительные числа больше 0')

    triangle_sides.sort()

    if (triangle_sides[0] + triangle_sides[1]) <= triangle_sides[2]:
        return print('составить из этих отрезков треугольник невозможно')

    if side_1 == side_2 and side_1 == side_3 and side_3 == side_2:
        return print(f'треугольник равносторонний')

    if side_1 == side_2 or side_1 == side_3 or side_3 == side_2:
        return print(f'треугольник равнобедренный')

    return print(triangle_sides , f' треугольник разносторонний')


check_triangle(input(f'введити длину сороны треугольника: '), input(f'введити длину сороны треугольника: '),
               input(f'введити длину сороны треугольника: '))
