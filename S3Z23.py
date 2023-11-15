# Задача №23. Общее обсуждение Дан массив, состоящий из целых чисел. Напишите программу, которая подсчитает количество элементов массива, больших предыдущего (элемента с предыдущим номером) Input: [0, -1, 5, 2, 3] Output: 2 (-1 < 5, 2 < 3)

# import random

# n = int (10)
# list = [random.randint(-2,5) for i in range(n)] 
# print (list)
# count = 0
# for i in range (1,len(list)):
#     if (list[i]>list[i-1]):
#         count+=1
# print(count)


# user_num = [0, -1, 5, 2, 3]
# count = 0
# for i in range(1, len(user_num)):
#     if user_num[i] > user_num[i - 1]:
#         count += 1
        
# print(count)


# user_num = [0, -1, 5, 2, 3]
# count = 0
# for i in range(len(user_num)-1):
#     if user_num[i] < user_num[i + 1]:
#         count += 1
        
# print(count)
