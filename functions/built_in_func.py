# встроенные функции

# input()
# print()
# str() etc.

# map()
# filter()
# lambda
# enumerate()

# анонимные  функции - lambda(такие же функции только без названия)
# lambda функции могут принимать сколько угодно аргументов но всегда возвращает только одно выражение

# ###################

# def sum_args(a, b):
#     res = a + b
#     return res

# def sum_args1(a, b): return a + b

# print(sum_args(1, 2))
# print(sum_args1(1, 2))

# sum_args2 = lambda a, b: a +b
# # x = int(input())
# print(sum_args2(1, 2))

# x = lambda a, b, c: (a * b) % c
# print(x (5, 7, 10))

# get_keys = lambda x: x.keys()
# dict_ = {1:'1', 2:'2', 3:'3', 4:'4', 5:'hi'}
# print(get_keys(dict_))


# ###################

# get_last = lambda ls: ls(-1)
# ls = [1, 2, 3, 4, 5,6 ,7, 8, 9, 'hello']
# print(get_last(ls))

# ###################

# def myfunc(n):
#     return lambda a: a * n

# myDoubler = myfunc(2)
# myTripler = myfunc(3)

# print(myDoubler(11))
# print(myDoubler(22))
# print(myTripler(11))
# print(myTripler(22))

# #################### 

# dict_ = {
#     'sanjar': 50000,
#     'john': 170000,
#     'aiany': 100000, 
#     'sultan': 10
# }

# new_dict = sorted(dict_.values())

# new_dict = sorted(dict_.items(), key = lambda x: x[1])
# print(new_dict)

# ls = ['just', 'guys', 'me', 'hello']
# print(sorted(ls, key=len))

# ---------------------------------------------------------

# map(function, Iterables) - применяет функцию к каждому элементу из последовательности и возращает  mapobject (итератор) с результатом.

# naprimer s pomoshyu map, mojno preobrazovyvat elementy. perevesti vse stroki v verhnyi nregistr

# ls = ['one', 'two', 'three', 'four', 'dict']
# result = map(str.upper, ls)
# print(result)

# #[ for i in result:
# #     print(i) ]

# result1 = list(map(len, ls))
# print(result1)

# /////////////////////////////////

# names = ['john', 'sultan', 'ayana']

# res = list(map(lambda x: f'hello mr/mrs {x}', names))

# print(res)

# dict_ = {1:2, 3:4, 5:6}
# res = dict(map(lambda x: (x[0], str(x[1])), (dict_.items())))
# print(res)

# dict_ = {k:str(v) for k,v in dict_.items()}
# print(dict_) # rauf's way

# -----------------------------------

# task 'craet passwords'

# from random import choices
# from string import ascii_letters,  digits, punctuation
# from itertools import repeat

# symbols = '_()+-!@#%'
# q_password = int(input('enter quantity of passwords: '))

# result = {f (choices(ascii_letters, k = 10), choices(digits, k=6), choices(symbols, k=2))
#     for f in repeat(lambda x, y, z: ''.join(set(x + y + z)), q_password)}

# print(result)
# print(f'quantity of passwords: {len(result)}')

# # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# from statistics import mean 

# dlina = [len(x) for x in result]
# print(f'middle len of password: {mean(dlina)}')

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# filter (function, iterable) -> приминяет ко всем элементам iterable функцию которую мы передали итератор с теми объектами для которых функция вернула True

# ls = ['one', 'two ', 'list', '', '100', '1', '50', 'john99', 'Rauf is silly! ']

# res = list(filter(str.isdigit, ls))
# print(res)


# ls = [10, 11, 102, 213, 314, 515]
# res = list(filter(lambda x: x % 2 != 0, ls))
# print(res)


# def func(stroka):
#     if len(stroka) >= 4:
#         return True
#     return False


# x = lambda stroka: len(stroka) >= 4

# ls = ['john', 'one', 'two', 'list', 'makers', 'py.22', 'ono']
# res = list(filter(func, ls ))
# res1 = list(filter(x, ls))
# print(res, res1)


# # enumerate(itarable) - returns 2 numbers(1-index, 2-element)

# ls = ['str2', 'str3']

# x = list(enumerate(ls))[1]
# print(x)

# for i, x in enumerate(ls):
#     print(f'index {i}, element {x}')

# zip(iterable) - она соединяет каждый элемент итерируемых объектов между собой в тип данных tuple и возвращает его

# ls1 = [1, 2, 3]
# ls2 = [100, 200, 300]

# res = list(zip(ls1, ls2)) # dict also works (if there are 2 elements)
# print(res)

# ls1 = [1, 2, 3, 4, 5]
# ls2 = [100, 200, 300, 4000, 500]
# ls3 = [10, 20, 30]
# res = list(zip(ls1, ls2, ls3))
# print(res)


# zip для создания словарей 
# x = [(1, 2)]
# a = dict(x)
# print(a)


# d_key = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# d_values = ['castle_r1', 'winter_fell', 'starks', 'cisco', '16.0', '10.255.0.1']

# res = dict(zip(d_key, d_values))
# print(res)


# d_key = ['hostname', 'location', 'vendor', 'model', 'IOS', 'IP']
# date = {
#     'r1':['london_r1', '21 new globe walk', 'cisco', '4451', '15.4', '101.25.0.1'],
#     'r2':['london_r2', '21 new globe walk', 'cisco', '4451', '15.4', '101.25.0.1'],
#     'sw1':['london_sw1', '21 new globe walk', 'cisco', '3850', '16.0', '55.251.0.101']
# }

# # res = dict(zip(d_key, list(date.items())))
# # print(res) # rauf's way 


# london_data = {}
# for k in date:
#     london_data[k] = dict(zip(d_key, date[k]))
# print(london_data)

# ----------------------------------

# all(), any()

# all(iterable) - возвращает True,если все элементы внутри объекты 

# ls = [[1, 2], 5, 'stroka', True, 1, '']
# print(all(ls))

# ip = '10.255.0.202'
# ip = '1p.20.12.101'
# ip = '155.1.1.100'
# print(all(ip))

# res = all(i.isdigit() for i in ip.split('.'))
# print(res)

# any - возвращает True, если хотя бы один элемент истинна

# ls = [0, 0, '', False, '123']
# print(any(ls))

# def ignore_command(command):
#     ignore_command = ['rm -rf', 'alias', 'reset']

#     for word in ignore_command:
#         if word in ignore_command:
#             return True
#     return False

# command = input('enter command: ')
# if ignore_command(command):
#     raise Exception('invalyd command! ')
# print('everything ok! ')


# ignore_command = ['rm -rf', 'alias', 'reset']
# command = input('enter command: ')
# if any([word in command for word in ignore_command]):
#     raise Exception('invalyd command! ')
# print('everything ok! ')

# def compareTriplets(a, b):
#     bob = 0
#     alice = 0
#     for i in range(0, len(a)):
#         if a[i] > b[i]:
#             alice +=1
#         elif b[i] > a[i]:
#             bob += 1
#     return [alice, bob]

