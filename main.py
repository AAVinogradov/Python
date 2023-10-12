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

firstNum = True
secondNum = 0
const = True
count = 0
while firstNum >= 0 and firstNum < 1000000:
    firstNum = int(input("Сколько потратил Вася в этом месяце: "))
    if firstNum < 0:
        break
    elif firstNum > secondNum:
        secondNum = firstNum
        count += 1
        const = True
    else:
        const = False
if count > 2 and const == True:
    const = True
else:
    const = False
print(const)