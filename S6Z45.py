# Задача №45. Решение в группах Два различных натуральных числа n и m называются дружественными, если сумма делителей числа n (включая 1, но исключая само n) равна числу m и наоборот. Например, 220 и 284 – дружественные числа. По данному числу k выведите все пары дружественных чисел, каждое из которых не превосходит k. Программа получает на вход одно натуральное число k, не превосходящее 105. Программа должна вывести  все пары дружественных чисел, каждое из которых не превосходит k. Пары необходимо выводить по одной в строке, разделяя пробелами. Каждая пара должна быть выведена только один раз (перестановка чисел новую пару не дает).

# Ввод: 300

# Вывод: 220 284

def sumDivisitors(num):
    div = (i for i in range(1, int(num / 2) + 1) if num % i == 0)
    # sum_ = sum(list(div))
    return sum(div)

def friendlyNums(num):
    newArray = (sorted([i,sumDivisitors(i)]) for i in range(4, num + 1)
                     if i == sumDivisitors(sumDivisitors(i)) and i !=sumDivisitors(i))
    friendlyArray = dict(newArray)
    return friendlyArray

def printFriendlyDict(dict_):
    for k,v in dict_.items():
        print(k,v)

k = int(input('Ведите число до которого будет осуществляться поиск: '))
printFriendlyDict(friendlyNums(k))