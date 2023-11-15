# Задача 30:  Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры. Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d. Каждое число вводится с новой строки.

# Ввод: 7 2 5 
# Вывод: 7 9 11 13 15

# def sequence_count(first_element, count_element):
#     sequence_list = []
#     elements_list = first_element
#     sequence_list.append(first_element)
#     i = 0
#     while i != count_element - 1:
#         elements_list += 1
#         sequence_list.append(elements_list)
#         i += 1
#     return sequence_list

# def arif_prog(first_element, sequence, step):
#     my_array = []
#     # my_array.append(first_element)
#     for i in range(len(sequence)):
#         element_af = first_element + ((i) * step)
#         my_array.append(element_af)
#     return my_array


# first = int(input("Введите первое число: "))
# step = int(input("Введите шаг арифметической прогрессии: "))
# count = int(input("Введите количество элементов: "))

# sequence = (sequence_count(first, count))
# print(sequence)
# print(arif_prog(first, sequence, step))


# Адаптация под автотест:
    
def sequence_count(first_element, count_element):
    sequence_list = []
    elements_list = first_element
    sequence_list.append(first_element)
    i = 0
    while i != count_element - 1:
        elements_list += 1
        sequence_list.append(elements_list)
        i += 1
    return sequence_list

def arif_prog(first_element, sequence, step):
    my_array = []
    # my_array.append(first_element)
    for i in range(len(sequence)):
        element_af = first_element + ((i) * step)
        my_array.append(element_af)
    return my_array


a1 = int(input("Введите первое число: "))
d = int(input("Введите шаг арифметической прогрессии: "))
n = int(input("Введите количество элементов: "))

sequence = (sequence_count(a1, n))
arithmetic_progression = (arif_prog(a1, sequence, d))
print(*arithmetic_progression, sep = "\n")