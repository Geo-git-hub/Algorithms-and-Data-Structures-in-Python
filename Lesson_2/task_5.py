"""
Вывести на экран коды и символы таблицы ASCII,
начиная с символа под номером 32 и заканчивая 127-м включительно.
Вывод выполнить в табличной форме: по десять пар "код-символ" в каждой строке.
"""
out_num = 1
for cod in range(32, 127 + 1):

    if out_num == 11:
        print('\n')
        out_num = 1

    print(f'Cod {cod} symbol {chr(cod)}', end='; ')

    out_num += 1
