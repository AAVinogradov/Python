# Задача №33. Решение в группах Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные. Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные. 
# Input: 5 -> 1 3 3 3 4 
# Output: 1 3 3 3 1

# ХЗ что это
# new_list = [i for i in range(5)]
# print(new_list)
# new_list.clear()  # new_list = []
# for i in range(5):
#     new_list.append(i)
# print(new_list)
# Сама задача

# Вариант 1
# n = int(input("Input count marks: "))
# marks = [int(i) for i in input("Input marks: ").split()[:n]]
# print([min(marks) if i == max(marks) else i for i in marks])

# # Вариант 2
# numbers = [1, 3, 3, 3, 4]
# def change_num(numbers):
#     min_num = min(numbers)
#     max_num = max(numbers)
#     for n in range(len(numbers)):
#         if numbers[n] == max_num:
#            numbers[n] = min_num
           
# change_num(numbers)
# print(*numbers)


# # Вариант 3
# vas_marks = [1, 3, 3, 3, 4]
# print([min(vas_marks) if i == max(vas_marks) else i for i in vas_marks])

# Вариант 4 через рекурсию

def grades_correction (array, i, max_num):
    if i == -1:
        return
    if array[i] == max_num:
        array[i] = min(array)
    return grades_correction (array, i - 1, max_num)

array = [1, 3, 3, 3, 4]
grades_correction(array, len(array)-1, max(array))
print(*array) 