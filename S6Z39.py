# Задача №39. Решение в группах Даны два массива чисел. Требуется вывести те элементы первого массива (в том порядке, в каком они идут в первом массиве), которых нет во втором массиве. Пользователь вводит  число N - количество элементов в первом массиве, затем N чисел - элементы массива. Затем число M - количество элементов во втором массиве. Затем элементы второго массива

# Ввод: 7 
# 3 3 2 12 3 1 3 4 2 4 12
# 6
# 4 15 43 1 15 1

# Вывод: 7 3 3 2 12

# (каждое число вводится с новой строки)

# Вариант 1:

# n = int(input("Введите количество элементов массива arr_n: "))
# arr_first=[]
# arr_second=[]
# arr_n=[]
# for i in range(n):
#     arr_n.append(int(input("Введите значение элементов массива: ")))
# m = int(input("Введите количество элемнетов массива arr_m: "))
# arr_m = []
# for i in range(m):
#     arr_m.append(int(input("Введите значения элементов массива: ")))
# for i in arr_n:
#     if i not in arr_m:
#         arr_first.append(i)
# print(arr_first)
# for i in arr_m:
#     if i not in arr_n:
#         arr_second.append(i)
# print(arr_second)

# Вариант через функции:

import random

def filter_list(array1, array2):
    res_array = []
    for i in array1:
        if i not in array2:
            res_array.append(i)
    return res_array

def create_random_list(number):
    return [random.randint(-10,10) for _ in range(number+1)]

number_1 = int(input("Введите количество элементов первого массива: "))
int_array_1 = create_random_list(number_1)
print(int_array_1)
number_2 = int(input("Введите количество элементов второго массива: "))
int_array_2 = create_random_list(number_2)
print(int_array_2)
print(filter_list(int_array_1, int_array_2))

# Решение в одну строку:
    
# def filter_list_2(array1, array2):
#     return [i for i in array1 if i in set(array1) - set(array2)]