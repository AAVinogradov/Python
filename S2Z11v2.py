# Задача №11. Решение в группах
# Дано натуральное число A > 1. Определите, каким по
# счету числом Фибоначчи оно является, то есть
# выведите такое число n, что φ(n)=A. Если А не
# является числом Фибоначчи, выведите число -1.
# Input: 5
# Output: 6

#0,1,1,2,3,5,8
    
a = int(input("Введите число: "))
first_fibo, second_fibo = 0, 1 
n = 2
while a > second_fibo:
    first_fibo, second_fibo = second_fibo, first_fibo + second_fibo 
    n += 1
if a == second_fibo:
    print(n)
else:
    print(-1)
    
# 0, 1
# 3 - first_fibo 1 second_fibo 1 
# 4 - first_fibo 1 second_fibo 2
# 5 - first_fibo 2 second_fibo 3
# 6 - first_fibo 3 second_fibo 5
