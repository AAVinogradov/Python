# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

# numberX = int(input("Введите число X "))
# numberY = int(input("Введите число Y "))
# temp = 0
# if numberX > numberY:
#     temp = numberY
#     numberY = numberX
#     numberX = temp
# if numberX > 1000 or numberY > 1000:
#     print("Не верно заданы входные значения!")
# else:
#     for x in range(numberX):
#         for y in range(numberY):
#             if numberX == x + y and numberY == x * y:
#                 first_num = y
#                 second_num = x
# print(f"{first_num} {second_num}")
               
# s = 11
# p = 28
# temp = 1
# while temp <= s // 2:
#     if (s - temp) * temp == p:
#         x = temp
#         break
#     temp += 1
# else:
#     x = 0
#     print("У задачи нет решения")
# if x > 0: 
#     y = s - x
#     print(x,y)


# s=6
# p=9

# d=s**2-4*p
# x=int ((s-d**(1/2))/2)
# y=int ((s+d**(1/2))/2)
# print (x, y)

# if (x!=y):
#     print (y,x)

 
# s = 6
# p = 9   
# x = (s - (s ** 2 - 4 * p) ** 0.5) / 2
# print(int(x), int(s - x))

x = (int(input("First number: ")))
y = (int(input("Second number: ")))

sum = x + y
print(f'Сумма чисел: {x + y}')
multiplicate = x * y
print(f'Произведение чисел: {x * y}')
if multiplicate == 0: print(sum, 0)
else:
    for i in range(1, sum):
        if (multiplicate % i == 0) and (sum - i == multiplicate / i): 
            print (i, sum - i, end="\n")
            break