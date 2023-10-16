#Сумма цифр трехзначного числа
n = 123
res = n // 100 + n % 100 // 10 + n % 10
print(res)

# n = 11111111111
# res = 0

# while n > 0:
#     digit = n % 10
#     if digit != 0:  
#         res += digit
#     n = n // 10

# print(res)

# for i in n:
#     i= int(i)
#     res+=i
# print(res)
