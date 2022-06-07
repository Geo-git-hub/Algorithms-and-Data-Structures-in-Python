"""
Определить количество различных подстрок с использованием хеш-функции. Задача: на вход
функции дана строка, требуется вернуть количество различных подстрок в этой строке.
Примечание: в сумму не включаем пустую строку и строку целиком.

"""

from hashlib import sha1


def count_substring(strings_dict, initial_string):
    initial_string_lenght = len(initial_string)

    for el in strings_dict:
        el_length = len(el)
        el_hash = sha1(el.encode("utf-8")).hexdigest()
        for i in range(initial_string_lenght - el_length + 1):
            subs_hash = sha1(initial_string[i:i + el_length].encode("utf-8")).hexdigest()
            if subs_hash == el_hash:
                strings_dict[el] += 1
    return strings_dict


def substrings_create_dict(user_string):
    str_length = len(user_string)

    if len(user_string) == 0:
        print("Строка не может быть пустой")
        exit(0)

    is_counted = [user_string]
    substrings = {}

    for start_s in range(str_length):
        for end_s in range(start_s + 1, str_length + 1):
            subs = user_string[start_s:end_s]
            if subs not in is_counted and subs not in substrings:
                substrings[subs] = 0

    substrings = count_substring(substrings, user_string)

    return substrings



user_input = input("Введите строку: ")
print(substrings_create_dict(user_input))
