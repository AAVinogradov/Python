# data = [{"V": "S001"}, {"V": "S002"},
# {"VI": "S001"}, {"VI": "S005"},
# {"VII": "S005"}, {"V":"S009"},
# {"VIII":"S007"}]
# set_values = set()
# # print(data[1])
# for i in data:
#     print(i)
# set_values.add(list(i.values())[0])
# print(set_values)

# number = int(input())

# while number <=100:
#     print(int(number/2))
#     number = int(input())

# n = None
# while n != 0:
#     n = int(input("Введите число: "))
#     if n == 0:
#         break
#     elif n % 2 == 0:
#         print(n)

# number = int(input("Введите дедлайн: "))
# while number > 0:
#     print(f"До дедлайна осталось {number} часов")
#     number -= 1
# if number == 0:
#     print("Пора сдавать работу, жопа с ручкой!")


# firstNum = 0
# secondNum = 0
# countMax = 0
# while firstNum >= 0 and firstNum < 1000000:
#     firstNum = int(input("Введите сколько Вася прожрал за эту неделю: "))
#     if firstNum > secondNum:
#         countMax = 1
#         secondNum = firstNum
#     elif firstNum < secondNum:        
#         next
#     elif firstNum == secondNum:
#         countMax += 1      
#     elif firstNum < 0:
#         break
# print(countMax)      

# price = int(input())
# max_price = price #максимальная стоимость обедов
# i = 0 #счетчик, кол-во самых дорогих обедов

# while 0 <= price < 1000000:
#     if price > max_price:
#         max_price = price
#         i = 1
#     elif price == max_price:
#         i += 1 
        
#     price = int(input())
# print(i)


# firstNum = 0
# secondNum = 0
# countMax = 0
# while firstNum >= 0 and firstNum < 1000000:
#     firstNum = int(input("Введите сколько Вася прожрал за эту неделю: "))
#     if firstNum > secondNum:
#         countMax = 1
#         secondNum = firstNum
#     elif firstNum == secondNum:
#         countMax += 1      
# print(countMax)   

# cost = int(input())
# next_cost = cost #затраты следующего месяца
# i = 0 #счетчик

# while 0 <= cost < 1000000:
#     if cost < next_cost:
#         next_cost = True
#         i = 1
#     elif cost >= next_cost:
#         next_cost = False
#         i += 1 
        
#     cost = int(input())
# print(next_cost)

# firstNum = 0
# secondNum = 0
# bool = True
# while firstNum >= 0 and firstNum < 1000000:
#     firstNum = int(input("Введите сколько Вася прожрал за эту неделю: "))
#     if firstNum > secondNum:
#         bool = True
#         secondNum = firstNum
#     elif firstNum <= secondNum:
#         bool = False      
# print(bool)   

# firstNum = True
# secondNum = 0
# const = True
# count = 0
# while firstNum >= 0 and firstNum < 1000000:
#     firstNum = int(input("Сколько потратил Вася в этом месяце: "))
#     if firstNum < 0:
#         break
#     elif firstNum > secondNum:
#         secondNum = firstNum
#         count += 1
#         const = True
#     else:
#         const = False
# if count > 2 and const == True:
#     const = True
# else:
#     const = False
# print(const)


# adress = input("Введите адреса через запятую без пробелов: ").split(',')
# print(adress)
# number = int(input("Введите количество замен: "))
# i = 0
# j = [0]
# f = [0]
# new_adress = list()
# while i < number:
#     input_adress = input("Введите старый и новый адрес через пробел: ").split(' ')
#     new_adress = new_adress + input_adress
#     i += 1
#     print(new_adress)
# for f in range (len(adress)):
#     for j in range (len(new_adress)):
#         if adress[f] == new_adress[j]:
#             adress[f] = new_adress[j + 1]
#             break            
# # print(*[item + ';' for item in adress])
# print(*adress, sep = ';')
# print()
# print("правильный результат: romashka@m.edu;zaika888@m.edu;121@m.edu;ooivanova@m.com;python_master@m.ru;taisia@m.edu")

# adress = input("Введите фамилии: ").split(',')
# number = int(input("Введите количество замен: "))
# for i in range (0, number, 1):
#     temp = input("Введите новый и старый адрес через пробел: ").split(' ')
#     old_add = temp[0]
#     new_add = temp[1]
#     for i in range(0, len(adress)):
#         if adress[i] == old_add:
#             adress[i] = new_add  
# print(*adress, sep = ';')

# adress = input().split(',')
# number = int(input())
# i = 0
# j = [0]
# f = [0]
# new_adress = list()
# while i < number:
#     input_adress = input().split(' ')
#     new_adress = new_adress + input_adress
#     i += 1
# for f in range (len(adress)):
#     for j in range (len(new_adress)):
#         if adress[f] == new_adress[j]:
#             adress[f] = new_adress[j + 1]
#             break            
# print(*adress, sep = ';')

# N1 = int(input())
# N2 = int(input())
# sq = None
# for i in range (N1, N2 + 1):
#     if i % 2 == 0:
#         sq = i * i
#         print(sq)
        
# N1 = int(input())
# N2 = int(input())
# sq =  [i * i for i in range(N1, N2 + 1) if i % 2 == 0]
# print(*sq, sep = "\n")


# cities = input().split(", ")
# letter = input()
# list1 = []
# temp_str = " "
# for i in range(len(cities)):
#     if cities[i] != 0:
#         temp_str = cities[i]
#         if temp_str[0] == letter:
#             list1.append(cities[i])
# print(*list1, sep = "\n")

def scholarship(grade):
    spisok_1_2 = []
    spisok_3 = []
    for i in grade:
        if i == 1 or i == 2:
            spisok_1_2.append(i)
        elif i == 3:
            spisok_3.append(i)
    if len(spisok_1_2) == 0 and len(spisok_3) == 1:
        return True
    else:
        return False

evaluations = [4, 5, 4, 4, 5, 3, 4, 5, 5, 5]
x = scholarship(evaluations)
print(x)
