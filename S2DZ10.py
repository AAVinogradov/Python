# Задача 10: На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом. Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки были повернуты вверх одной и той же стороной. Выведите минимальное количество монет, которые нужно перевернуть


quantityСoins = int(input("Введите количество монет: "))
import random
# coins = [random.randint(0, 1) for i in range(quantityСoins)]
coins = []
for i in range(quantityСoins):
    coins.append(random.randint(0, 1))
print(coins)
i = 0
sum1 = 0
sum2 = 0
for i in coins:
    if i == 1:
        sum1 += 1
        
    elif i == 0:
        sum2 += 1
print(f"{sum1} монет(-ы -а) лежит вверх решкой")
print(f"{sum2} монет(-ы -а) лежит вверх орлом")
if sum1 >= sum2:
    print(f"Нужно перевернуть {sum2} орла (-ов)")
else:
    print(f"Нужно перевернуть {sum1} решеки(-у -ек)")