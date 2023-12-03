# Напишите функцию print_operation_table(operation, num_rows, num_columns), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца.
# Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны.
# Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля).
# Если строк меньше двух, выдайте текст
# ОШИБКА! Размерности таблицы должны быть больше 2!.
# Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.
# Пример
# На входе:
# print_operation_table(lambda x, y: x * y, 3, 3)

# На выходе:
# 1 2 3
# 2 4 6 
# 3 6 9

# Задача 36:  Напишите функцию print_operation_table(operation, num_rows=6, num_columns=6), которая принимает в качестве аргумента функцию, вычисляющую элемент по номеру строки и столбца. Аргументы num_rows и num_columns указывают число строк и столбцов таблицы, которые должны быть распечатаны. Нумерация строк и столбцов идет с единицы (подумайте, почему не с нуля). Примечание: бинарной операцией называется любая операция, у которой ровно два аргумента, как, например, у операции умножения.

# Ввод:
#     print_operation_table(lambda x, y: x * y) 
# Вывод:
#     1  2  3  4  5  6
#     2  4  6  8  10 12
#     3  6  9  12 15 18
#     4  8  12 16 20 24
#     5  10 15 20 25 30
#     6  12 18 24 30 36  

# Вариант 1: 
def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2 :
        return print("ОШИБКА! Размерности таблицы должны быть больше 2!")
    print(" ".join([str(k) for k in range(1, num_columns + 1)]))
    for i in range(2, num_rows + 1):
        s = " ".join([str(operation(i, j)) for j in range(2, num_columns + 1)])
        print(str(i) + " " + s)

print_operation_table(lambda x, y: x - y, 5, 5)


# # Вариант 2 (не для проверки): 
# def print_operation_table(operation, num_rows, num_columns):
#     if num_rows < 2 or num_columns < 2:
#         return print("ОШИБКА! Размерности таблицы должны быть больше 2!")
#     else:
#         for i in range(1, num_rows + 1, 1):
#             for j in range(1, num_columns + 1, 1):
#                 print (operation(i, j), end = " ")
#             print (" ")
# print_operation_table(lambda x, y: x * y, 4, 4)

# Вариант 3
def print_operation_table(operation, num_rows, num_columns):
    if num_rows < 2:
        print('ОШИБКА! Размерности таблицы должны быть больше 2!')
    else:
        for i in range(1,num_rows+1):
            if i == 1:
                sq = [i for i in range(1,num_rows+1)]
            else:
                sq = [operation(i,j) if j > 1 else i for j in range(1, num_columns + 1)]
            print(*sq)

