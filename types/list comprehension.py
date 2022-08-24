# list comprehension - generatory spiskov 

# list comprehensions - uprishennyi podhod k sozdaniyu spiskov, kotoryi zadeistvuyut tsikl for, a takje konstruktsii if esle lya opredeleniye togo, chto v itoge okajetsya dobavleno v nash spisok 
# comprehent - only one cod, terner
############################

# ls = []
# for i in range(0, 200):
#     if i % 2 == 0:
#         ls.append(i)
# print(ls)

# ls = [i for  i in range(0, 200) if i % 2 == 0]
# print(ls)

############################
# ls = []
# for i in range(0, 300):
#     if i % 2 == 0 and i % 3 == 0:
#         ls.append(i)
# print(ls)

# ls = [i for i in range(0, 300) if i % 2 == 0 and i % 3 == 0]
# print(ls)
############################
# ls = []
# for i in range(0, 100):
#     if i % 2 == 0:
#         ls.append(i ** 2)
#     else:
#         ls.append(i)
# print(ls)

# ls = [i**2 if i % 2 == 0  else i for i in range(0, 100)]
# print(ls)
 
# # -----------------------------------------------------------------------------------------

# newlist = [expression for otem in itarable <if condition == True>]

# ls = []
# for i in range(0, 100, 2):
#     ls.append(i)
# print(ls)

# ls = [i for i in range(0, 100, 2)] # sleva for dobavleniye v (i)
# print(ls)

# ls = [i**2 for i in range(0, 11)]
# print(ls)

# fruits = ['apple', 'banana', 'kiwi', 'mango', 'limon']
# ls = [i.capitalize() for i in fruits]
# print(ls)

# ls = [i for i in fruits if 1] # if there True
# print(ls)

# ls = [i for i in fruits if i != 'apple']
# print(ls)


#@@@@@@@@@@@@@@@@@@@@

# 1 - way
# ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = []
# for inner_list in ls:
#     # print(inner_list)
#     for i in inner_list:
#       result.append(i)
# print(result)
# 2 - way
# result = []
# for i in ls:
#     result.extend(i)
# print(result)
# 3 - way
# result = []
# for i in ls:
#     result += [*i]
# print(result)
# 4- way
# ls = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
# result = [i for inner in ls for i in inner]
# print(result)
# ---------------------------------------------------------------------
# from  datetime import datetime
# ls = []
# ls =[i for i in range(0, 1000000) ]
# start = datetime.now()
# # print(start)
# # for i in range(0, 100_000_000):
# #     ls.append(i)
# finish = datetime.now()
# print(ls)

 

# ls = [i + 10 if i == 8 else i + 100 for i in range(0, 10)]
# print(ls)

# -----------------------------------------------------------------------
# dict coprehensions

# dict_ = {
#     'key': 'value',
#     'key1': 'value2'
# }

# dict_ =  {n: n**2 for n in range(0, 10)}
# print(dict_)


# dict_ = {i: i **3 for i in range(1, 15)}
# print(dict_)

# di = {
#     '2':1, 
#     'b':2, 
#     'c':3, 
#     'd':4, 
#     'e':5, 
#     'f':6, 
#     'g':7, 
#     'h':8
# }

# nd = {k: 'even' if v % 2 == 0 else 'odd' for k, v in di.items()}
# print(nd)

# names = ['John', 'Tireo', 'Jemy', 'Sam', 'Harry']
# dname = {i: value for i, value in enumerate(names)}
# # # print(dname)
# a = [1, 2, 3, 4, 5]
# b = []
# for i, v in enumerate(a): # shows an index
#     b.append(i)
#     b.append(v)
# print(b)
