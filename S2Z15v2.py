# Задача №15. Решение в группах
# 15. Иван Васильевич пришел на рынок и решил
# купить два арбуза: один для себя, а другой для тещи.
# Понятно, что для себя нужно выбрать арбуз
# потяжелей, а для тещи полегче. Но вот незадача:
# арбузов слишком много и он не знает как же выбрать
# самый легкий и самый тяжелый арбуз? Помогите ему!
# Пользователь вводит одно число N – количество
# арбузов. Вторая строка содержит N чисел,
# записанных на новой строчке каждое. Здесь каждое
# число – это масса соответствующего арбуза
# Input: 5 -> 5 1 6 5 9
# Output: 1 9

# lst = list(map(int, input("введите числа через пробел: ").split(" ")))
# print(min(lst), max(lst))

# n = int(input('Введите количество арбузов: '))

# weight_min = 100
# weight_max = 0
# for i in range(n):
#     weight = int(input(f'Введите вес {i + 1} арбуза: '))
#     if weight > weight_max:
#         weight_max = weight
#     if weight < weight_min:
#         weight_min = weight
# print(f'Самый легкий арбуз {weight_min} кг, самый тяжелый {weight_max} кг')

from random import randint
n = int(input('Введите количество арбузов: '))
watermelons = []
for i in range(n):
    watermelons.append(randint(1, 100))
print(watermelons)
print(f"Минимальный арбуз {min(watermelons)}")
print(f"Максимальный арбуз {max(watermelons)}")

r = randint(1, 100)
print(f"Рандомное число r - {r}")
