# По данному целому неотрицательному n вычислите значение n!. N! = 1 * 2 * 3 * … * N (произведение всех чисел от 1 до N) 0! = 1 Решить задачу используя цикл while
# Input:       5
# Output:    120

n = int(input("Введите число N: "))
f = 1
while n > 0:
    f = f * n       
    n = n - 1       
print(f)

# n = int(input("Input number: "))
# result = 1
# while n > 1:
#     result *= n # result = result * n
#     n -= 1
# print(result)