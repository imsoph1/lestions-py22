# while expression:
#   <body>

# i = 1
# while i <= 10:
#     print(f'tsikl vypolnitsya {i} raz! ')
#     i += 1 # i  = i + 1

# name1 = ''
# name2 = ''
# i = 0

# while name1.lower() != 'john' or name2.lower() != 'raychel':
#     name1 = input('vvedite imya1: ')
#     name2 = input('vvedite imya2: ')
#     i += 1   # i  = i + 1
#     if i > 5:
#         print('tsikl ostanovlen!')
#         break
# else:
#     print('vy vveli pravilnoe imya! ')

# admin = ['John', 'ilovepython123']
# i = 3
# password = None

# while admin[1] != password:
#     password = input(f'{admin[0]}  vvedite parol\' : ')
#     i -= 1
#     if i == 0:
#         print('vy zablokirovany! ')
#         break
# else:
#     print(f'{admin[0]} vy uspeshno zashli! ')


# for < variable> in <iteravle object>:
#     <body>
# ///////////// inter////////////////

# list_ = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
# i = iter(list_)
# print(i)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))


# for i in list_[::-1]:  # naoborot
#     print(i)

# domashka///////////////
# list_ = []
# num = input('Enter: ').split(',')
# for i in num:
#   list_.append(int(i))
# list_[-1] = 'makers'
# print(list_)

# num = []
# kol_num = 7
# for i in range(kol_num):
#   chislo = input('vvedite chislo: ')
#   num.append(int(chislo))
# print(num[0], num[-1])
# num[-1] = 'Makers'
# print(num)
# ////////////////////////////////////////

# secret_list = ['DeltaViski', 'LOT123', 'TwentyTwoRiders']
# nick = input('vvedite svoi nick: ')

# while nick not in secret_list:
#     print('incorrect  nick! Try one more time: ')
#     nick = input('vvedite svoi nick: ')
# else:
#     print(f'you\'re welcome my dear friend!, {nick}')

# 6 = [3, 1 6, 2]
# 23436, 190_200, 380_457_890_232

# number1 = 100

# result =[1, number1]

# for i in range(2, int(number1 ** 0.5)+ 1):
#     if number1 % i == 0:
#         result.extend({i, number1 // i})
# result.sort()
# print(result)

# 2- version 
# ////////////////////////// write here photo
# import random 
# ls = []
# for x in range(1, 100):
#     ls.append(random.randint(1, 15))
# print(sorted(ls))
# res = list(set(ls))
# print(res)


