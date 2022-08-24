# Тип данных int()

#number = 5 # number - переменная 

# + 
# a = 10 
# b = 5
# result = a + b
# print(result)
# print(a + 100)

# a = 10 
# b = 60 
# c = 100
# d = 1000000
# e = 50
# print(a + b + c + d + e)

# / and //
#5 / 2 = 2.5 -> float()
#5 // 2 = 2 ->целочисленное деление 
# num1 = 25
# num2 = 12
# print(num1 / num2)
# print(num1 // num2)

# *
# % - деление при котором мы получим остаток 
# a = 5 
# b = 2 
# result = a % b
# print(result)

# ** -> возведение в степень 
# 5 ** 4 = 625
# 5 ** 2 = 5 * 5 = 25 
# print(2 ** 4)
 
# a = 5 
# b =3 
# result = pow(a, b)
# print(result)
# print(pow(a, b))

# print(pow(5, 2, 12))
# round() - округление числа с плавающей точкой 

# a = 5.723232
# result = round(a, 2)
# print(result)

#abs() - абсолютное значение -> abc(-5) - 5
# |-5| = 5 

# a = abs(-16)
# print(a)

#divmod(a, b) - Она выводит два числа, первое число это результат целочисленного деление (//) a на b. Второе число это мольное деление(%)a на b.

# result = divmod(5, 2)
# print(result)

# import math 

# a = 5 
# print(math.sqrt(a))

# chislo_py = math.pi
# print(chislo_py) 

# ////////////////////////////////////////////////////////
# Множественное присваивание
# оператор присваивание 

# a, b, c = 1, 2, 5
# print(a)
# print(b)
# print(c)

# a, b, c = c, a, b
# print(a, b, c)
# from math import pi
# r = int(input('vvidite radius: '))
# result_P = 2 * pi * r
# result_S = pi * (r ** 2)
# print('площадь окружност', round(result_S, 2))
# print('площадь окружност', round(result_P, 2))

#'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

# num = 6 
# num = 'string'
# print(num)
# print(type(num))

# num = 5
# str1 = ' hello world'
# print(str * num) 
 
# num = 5
# str1 = '116'
# print(str1 + str(num))
# num2 = int(str1)
# print(type(num2))

# num = 5 
# str1 = 'John Snow'
# print(str1 + str(num))

# num1 = int(input('vvedite chislo: '))
# num2 = int(input('vvedite stepen: '))
# print(num1 ** num2)
# print(pow(num1, num2))

#import random 

# import random
# name = input('vvrditr svoe imya:')
# last_name = input('vvrditr svoyu familiyu: ')

# num = str(random.randint(111111, 999999))
# num = set(num)
# print(num)
# num = '@' .join(list(num))
# print(num)

# result = name + last_name + str(num)
# print(result)

# a = 1
# b = a
# print(id(a))
# print(id(b))
# print(id(1))

# dict_ = {1:'justme', 2:'helloguys'}
# dict_ = {value: key for key, value in dict_.items()}
# print(dict_)
# try:
#     username = input('enter username: ')
#     username_id = dict_[username]
#     print(username_id)
# except KeyError:
#     print('there is no such username in datebase! ')
# else:
#     print(f'welcome {username}')
# finally:
#     print('thank you ')

# try:
#     age = int(input('enter ur age:' ))
#     if age <= 0:
#         raise Exception('do not enter negative or zero ')
# except ValueError:
#     print('enter integer not string! ')
# else:
#     print(f'your age: {age}' )

