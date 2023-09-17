# Задача 12: Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница. Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать. Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P. Помогите Кате отгадать задуманные Петей числа.

numberX = int(input("Введите число X "))
numberY = int(input("Введите число Y "))
temp = 0
if numberX > numberY:
    temp = numberY
    numberY = numberX
    numberX = temp
if numberX > 1000 or numberY > 1000:
    print("Не верно заданы входные значения!")
else:
    for x in range(numberX):
        for y in range(numberY):
            if numberX == x + y and numberY == x * y:
                print(f"Первое число = {x}, второе число = {y}")

