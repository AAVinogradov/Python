# Задача №21. Решение в группах Напишите программу для печати всех уникальных значений в словаре. Input:  [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII ":" S007 "}] Output: {'S005', 'S002', 'S007', 'S001', 'S009'}


data = [{"V": "S001"}, {"V": "S002"},
         {"VI": "S001"}, {"VI": "S005"},
           {"VII": "S005"}, {"V":"S009"},
             {"VIII":"S007"}]
set_values = set() 
# print(data[1])
for i in data:
    print(i)
    set_values.add(list(i.values())[0])
print(set_values)


# dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"},
#               {"VII": " S005 "}, {" V ":" S009 "}, {" VIII": " S007 "}]

# list = []

# for i in range(len(dictionary)):
#     for j in dictionary[i]:
#         if dictionary[i][j] not in list:
#             list.append(dictionary[i][j])
# print("Вот все уникальные значения которые есть в словаре; ",list)


# dictionary = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}]
# list_ = []

# for i in dictionary:
#     for j in i:
#         if i[j].strip() not in list_:
#             list_.append(i[j].strip())
# print("Вот все уникальные значения которые есть в словаре; ",list_)


# user_list = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
# {"VI": "S005"}, {"VII": " S005 "}, {" V ":" S009 "}, {" VIII":" S007 "}] 
# result = set(v.strip() for i in user_list for v in i.values())
#print(result)