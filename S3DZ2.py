import random

N = int(input("Введите количество элементов в массиве "))
list_1 = [random.randint(1, 20) for i in range(N)]
print(list_1)
k = int(input("Введите искомое число "))
count = 0
min_element = abs(k - list_1[0])
for i in range(1, N):
    temp = abs(k - list_1[i])
    if temp < min_element:
        min_element = temp
        count = i

print(f"Самый близкий по величине элемент к заданному числу {list_1[count]}")
    


# m = abs(k - list_1[0])  # модуль числа
# number = list_1[0]
# for i in range(1, len(list_1)):
#     if m > abs(list_1[i] - k):
#         m = abs(list_1[i] - k)
#         number = list_1[i]
# print(number)