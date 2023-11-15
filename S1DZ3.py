# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета с номером n и выводит на экран yes или no.

ticket = int(input("Введите шестизначный номер билета: "))
x = len (str (ticket))
if x != 6:
    print("Вы ввели некорректный номер билета")
else:
    count1 = int(str(ticket)[0]) + int(str(ticket)[1]) + int(str(ticket)[2])
    count2 = int(str(ticket)[3]) + int(str(ticket)[4]) + int(str(ticket)[5])
    if count1 != count2:
        print(f"Билет № {ticket} счастливый?")
        print("Нет")
    else:
        print(f"Билет № {ticket} счастливый?")
        print("Да")
        


# n=str(n)
# res = 0
# res1 = 0
# for i in range(len(n)//2):
#     res += int(n[i])
#     res1 += int(n[len(n)//2 + i])
# if res == res1:
#     print('yes')
# else:
#     print('no')

# n = 12321
# n=str(n)
# res = 0
# res1 = 0
# for i in range(len(n)//2):
#     res += int(n[i])
#     res1 += int(n[len(n)//2 + i])
# if res == res1:
#     print('yes')
# else:
#     print('no')

# n = 385916
# n = str(n)
# sum1=int(n[0])+int(n[1])+int(n[2])
# sum2=int(n[3])+int(n[4])+int(n[5])
# if sum1==sum2:
#   print('yes')
# else:
#   print('no')

# n1 = n // 100000
# n2 = (n % 100000) // 10000
# n3 = (n % 10000) // 1000
# n4 = (n % 1000) // 100
# n5 = (n % 100) // 10
# n6 = n % 10
# if n1 + n2 + n3 == n4 + n5 + n6:
#     print('yes')
# else:
#     print('no')