# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

count = int(input("Введите число "))
maxCountInt = 2147483647
if count > maxCountInt:
    print("Превышено максимальное значение типа данных Int")
r = range(0, count, 1)
for x in r:
    p = 2 ** x
    if p < count:
        print(p)