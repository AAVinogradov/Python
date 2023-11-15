# # Задача 18: Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. В последующих  строках записаны N целых чисел Ai . Последняя строка содержит число X

# 5 
# 1 2 3 4 5 
# 6
# -> 5

n = int(input("Введите длинну списка: "))
x = int(input("Введите число X: "))
import random
list_1 = [random.randint(0,10) for i in range(n)] 
print(list_1)
num_min = abs(x - list_1[0])
for i in range(len(list_1)):
    mod_num = abs(x - list_1[i])
    if mod_num < num_min:
        num_min = mod_num
        count = list_1[i]
print(f"Близкий элемент по величине к числу Х - это число {count}")
       
            
