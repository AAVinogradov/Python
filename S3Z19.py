# Задача №19. Решение в группах Дана последовательность из N целых чисел и число K. Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо,  K – положительное число. Input:   [1, 2, 3, 4, 5] k = 3 Output:  [4, 5, 1, 2, 3]

list_num = [1, 2, 3, 4, 5]
k = 3

print(list_num)
for i in range(k):
    list_num.insert(0, list_num.pop())
    
print(list_num)

# list_num = [1, 2, 3, 4, 5]
# k = 3
# print(list_num[:k])
# print(list_num[k:])

# print(list_num[k:] + list_num[:k])




# list_1 = [45, 23, 1, 5, 31] # len()
# k = int(input("Введите кол-во сдвигов: ")) % len(list_1)
# # int.Parse(Console.ReadLine()!) % array.Length;
# # print(list_1[begin=0:end=обязательный_парамет:step=+1])
# if k == 0:
#     print(list_1)
# else:
#     print(list_1[-k:] + list_1[:len(list_1) - k])