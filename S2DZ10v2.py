
n = int(input("Введите кол-во монет: "))
count_zero = 0
count_one = 0
for i in range(n):
    x = int(input("Введите сторону монеты(1 или 0): "))
    if x == 1:
        count_one += 1
    else:
        count_zero += 1
if count_zero > count_one:
    print(count_one)
else:
    print(count_zero)