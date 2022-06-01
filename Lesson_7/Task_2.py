"""
Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный
случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный
массивы.


"""
import random

size = random.randint(2, 10)

init_lst = [random.random() * 50 for i in range(size)]
print(f'Исходный список \n{init_lst}')


def merge_list_sort(lst):
    if len(lst) == 1:
        return lst

    half = len(lst) // 2
    list_1 = merge_list_sort(lst[:half])
    list_2 = merge_list_sort(lst[half:])

    def sort_two_list(lst_1, lst_2):

        reuslt = []
        i = 0
        j = 0

        while i < len(lst_1) and j < len(lst_2):

            if lst_1[i] < lst_2[j]:
                reuslt.append(lst_1[i])
                i += 1
            else:
                reuslt.append(lst_2[j])
                j += 1

        if i < len(lst_1):
            reuslt += lst_1[i:]

        if j < len(lst_2):
            reuslt += lst_2[j:]

        return reuslt

    return sort_two_list(list_1, list_2)


result_list = merge_list_sort(init_lst)
print(f'Отсортированный список \n{result_list}')
