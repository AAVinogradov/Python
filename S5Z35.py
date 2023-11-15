# # Задача №35. Решение в группах Напишите функцию, которая принимает одно число и проверяет, является ли оно простым Напоминание: Простое число - это число, которое имеет 2 делителя: 1  и n(само число) 
# # Input: 5 
# # Output: yes




# def is_prime(n):
#     for i in range(2, int(n ** 0.5) + 1):
#         if n % i == 0:
#             return False
#     return (n != 1) * True


# print('yes' if is_prime(int(input("Input number: "))) else 'no')


# # Вариант 2

# def prime_num(n):
#     if n <= 1:
#         return False
#     for i in range(2, n // 2 ):
#         if n % i == 0:
#             return False
#     return True
# print(prime_num(n))


# Вариант 3 через рекурсию

def prime_num(n, i = None):
    if i is None:
        i = n-1
    if i == 1:
        return "Yes"
    if (n <= 1) or (n % i == 0):
        return "No"
    
    return prime_num(n, i-1)
    

print(prime_num(-1)) #меняется значение тут

