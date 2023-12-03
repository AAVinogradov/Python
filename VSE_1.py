import time
start = time.time()
# print(start)
res = [i * 2 for i  in range(10000000)]
# for i in range(10000000):
#     res.append(i * 2)
# # print(res)
print(time.time() - start)




# import time
# import sys
# start = time.perf_counter()
# # print(start)
# # res_ = [i * 2 for i in range(10000000)]  # 0.38088374200015096
# res_2 = (i * 2 for i in range(3))  # 0.0000039
# # res = []
# # for i in range(10000000):
# # #     i  # 0.22269944800063968
# #     res.append(i * 2)
# # print(res)
# # 81528048
# #      112
# print(time.perf_counter() - start)  # 0.7289290859989705
# print(sys.getsizeof(res_2))
# # print(res_2)
# # print(type(res_2))
# print('next:', next(res_2))
# for j in res_2:
#     print(j)
# print('next2:', next(res_2))




