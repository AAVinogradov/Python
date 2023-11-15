# Требуется вычислить, сколько раз встречается некоторое число k в массиве list_1.

# Найдите количество и выведите его.

# Пример:


# list_1 = [1, 2, 3, 4, 5]
# k = 3
# # 1

n = int(input("Введите длинну списка: "))
p = int(input("Введите число: "))
k = 0
import random
list_1 = [random.randint(0,10) for i in range(n)] 
print(list_1)
for j in range(len(list_1)):
    if p == list_1[j]:
        k += 1
print(k)