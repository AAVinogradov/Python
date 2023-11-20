# Задача 24: В фермерском хозяйстве в Карелии выращивают чернику. Она растет на круглой грядке, причем кусты высажены только по окружности. Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов. Эти кусты обладают разной урожайностью, поэтому ко времени сбора на них выросло различное число ягод – на i-ом кусте выросло ai ягод. В этом фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Собирающий модуль за один заход, находясь непосредственно перед некоторым кустом, собирает ягоды с этого куста и с двух соседних с ним. Напишите программу для нахождения максимального числа ягод, которое может собрать за один заход собирающий модуль, находясь перед некоторым кустом заданной во входном файле грядки.
# 4 -> 1 2 3 4 
# 9

# В фермерском хозяйстве в Карелии выращивают чернику. Черника растет на круглой грядке, и кусты черники высажены по окружности грядки. Каждый куст черники имеет урожайность, которая соответствует количеству ягод на этом кусте.

# Урожайность черничных кустов представлена в виде списка arr, где arr[i] - это урожайность (количество ягод) i-го куста.

# В фермерском хозяйстве внедрена система автоматического сбора черники. Эта система состоит из управляющего модуля и нескольких собирающих модулей. Каждый собирающий модуль может собрать ягоды с одного куста и с двух соседних кустов. Собирающий модуль находится перед определенным кустом, и он может выбирать, с какого куста начать сбор ягод.

# Ваша задача - написать программу, которая определит максимальное число ягод, которое может собрать один собирающий модуль за один заход, находясь перед некоторым кустом грядки.

# Входные данные:

# На вход программе подается список arr, где arr[i] (1 ≤ arr[i] ≤ 1000) - урожайность i-го куста черники. Размер списка не превышает 1000 элементов.

# Выходные данные:

# Программа должна вывести одно целое число - максимальное количество ягод, которое может собрать собирающий модуль, находясь перед некоторым кустом грядки.

# Пример использования На входе:
# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# На выходе:
# 19

# n = int(input("Введите количество кустов: "))
# if n >= 1000 or n < 1:
#     print("Не верно заданы значения")
# else:
#     import random
#     list_1 = [random.randint(1,5) for i in range(n)] 
#     print(list_1)
#     list_2 = list_1
#     last_count = list_1[0]
#     last_count_2 = list_1[1]
#     list_2.append(last_count)
#     list_2.append(last_count_2)
#     max_berry = list_2[0] + list_2[1] + list_2[2]
#     print(list_2)
#     # print(first_bush)
# for i in range (len(list_2)-2):
#     next_bush = list_2[i] + list_2[i + 1] + list_2[i + 2]
#     if next_bush > max_berry:
#         max_berry = next_bush
# print(max_berry) 
    

# arr = [5, 8, 6, 4, 9, 2, 7, 3]
# # Введите ваше решение ниже
# n = int(input("Введите количество кустов: "))
# if n >= 1000 or n < 1:
#     print("Не верно заданы значения")
# else:
# #     import random
# #     list_1 = [random.randint(1,5) for i in range(n)] 
#     # print(arr)
#     list_2 = arr
#     last_count = arr[0]
#     last_count_2 = arr[1]
#     list_2.append(last_count)
#     list_2.append(last_count_2)
#     max_berry = list_2[0] + list_2[1] + list_2[2]
#     print(list_2)
#     # print(first_bush)
# for i in range (len(list_2)-2):
#     next_bush = list_2[i] + list_2[i + 1] + list_2[i + 2]
#     if next_bush > max_berry:
#         max_berry = next_bush
# print(max_berry) 

arr = [5, 8, 6, 4, 9, 2, 7, 3]

list_2 = arr
last_count = arr[0]
last_count_2 = arr[1]
list_2.append(last_count)
list_2.append(last_count_2)
max_berry = list_2[0] + list_2[1] + list_2[2]
# print(list_2)
for i in range (len(list_2)-2):
    next_bush = list_2[i] + list_2[i + 1] + list_2[i + 2]
    if next_bush > max_berry:
        max_berry = next_bush
print(max_berry) 
    
    
    