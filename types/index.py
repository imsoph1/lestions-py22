# Типы данных в питоне:
# 1. NoneType -> Ничего, пустота
# None #NoneType

# a = None 
# print(a)
# 2. Boolean -> Правда или Ложь (True/False)
# True = 1
# False = 0
#"""'''''
# 3. Числовые типы данных:
#"""
       # a. integer(int) -> Челое число(1,2,3,4,5)
       # b. float() -> Число с плавающей точкой(1.2, 10.20,2.7)
       # c. complex() -> Комплексные числа(3+5i/j)
# 4. Списковые типы данных:
       # a. list(список/массив) -> [1, 2, 3, True, None]
       # b. tuple(кортеж) -> (1,2,3,False)
       # c. range(последовательность) -> range (1,5) -> 1,2,3,4
# 5. string(str) строка -> "hello world"
                        #'helo world'

# john = 'my name is John' 
# 
# 6. set() -> Множество
# 7. dict (словари) -> содержит данные в виде ключа: значение -> {1: 'one', 2: 'two'}

# **********************************************************************************

# mutable(изменяемые типы данных)
# 1. list() izmenyz, uporyad
# 2. set{} unique, neupor
# 3. dict{} unique

# immutable(неизменяемые типы)
# 1. None
# 2. bool(true, false)
# 3. int(), float(), complex()
# 4. str()
# 5. range()
# 6. tuple()neizmenyaem, 
# **********************************************************************************

#''''''
# В пайтоне для вывода данных в терминал используется функция print()

#print('hello world my name is John')
#''''''
# стандартный ввод данных
#''''''
# для ввода исользуется функция input()
#''''''
# a = input(' введите число: ')
# print(a)
# # type() выводит тип данных
# print(type(a))
# b = int(input('введите число номер 2: '))
# print(b)
# print(type(b))
# /////////////////////////////////////////////////////////
# from random import randint
# sum = 0
# n = int(input('vvedite chislo: ' ))
# for i in range(n):
#        a = randint(23, 345)
#        sum += a
#        print(a)
# print()
# print(sum)
#########################
# n = int(input())
# for i in range(n):
#        print(2**i)
 
# n = int(input())
# s = 0
# for i in range(n):
#        a = int(input())
#        s += a
#        print('current s', s)
# print('total', s)
# print('mid.score', s/n)


#---------------------------

# number = input('enter numbers via comma: ').split(',')
# # print(number)
# int_ = []
# for i in number:
#        int_.append(int(i))
# print(int_[0], int_[-1])

# int_.pop()
# int_.append('makers')
# print(int_)


# from random import randint
# n = int(input())
# for i in range(n):
