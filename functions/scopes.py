# область видимости и пространства имен scopes определяет переменной, в рамках которого мы можем ее импользовать.
# built-in (встроенная) - print, len, max
# global (глобальная)
# enclosed (локальная область)

# def myfunc():
#     x = 300
#     print(x)

# myfunc()
# print(x)

# ##############

# x = 10 # global
# print # built- in
# def hello(): # global
#     x = 'hello world' # local
#     print(x, 'local inside at func')

# hello()
# print(x, 'global')

# ###############

# x = 'global'
# print(x, '1')

# def enclosed(): #global
#     x = 'enclosed'
#     def local(): # local
#         x = 'local'
#         print(x, '3')
#     print(x, '2')
#     local()
#     print(x, '4')

# enclosed()
# print(x, '5')

# ################

# LEGB
# local - enclosed - global - built-in 

# len = 5
# len()
# print(len([1, 2, 3, 4, 5, 6, 7, 8]))

# #############
# ERROR

# a = 10

# def func():
#     print(a)
#     a = 15
#     print(len)

# func()

# var = 100 #global variable
# x = 5

# def increment():
#     var += 1 # try to update a global variable inside local scope
#     print(var)
#     x = 10
# increment()
# we can print local but not change!


# global -> позваляет изменять значения глобальной переменной находясь в локальной области видимости.

# nonlocal -> позваляет изменять значения нелокальной  переменной находясь в локальной области видимости.

# var = 100

# def increment():
#     global var # 
#     var += 1 # var = var + 1

# print(var)
# increment()
# increment()
# increment() # 103
# print(var)

# #####################

# def counter():
#     num = 0
#     def increment():
#         nonlocal num 
#         num += 1
#         return num 
#     return increment

# c = counter()
# print(c()) # 1
# print(c()) # 2
# print(c()) # 3
# print(c()) # 4
# b = counter()
# print(b()) # 1
#  print(c()) # 5

# i =

# for x in range(0, 10000):
#     if x % 3 == 0 and x % 5 == 0:
#         print(i)

# ###########
# print(dir(__builtins__))
# print(len(dir(__builtins__)))

# print(abs(-15)) # стандартный вызов встроенной функции
# abs = 10 # переопределяем встроенное имя abs 
# # print(abs(-15))
# del abs
# print(abs(-35))
# print(abs)

# print(globals()) # shows globals and locals 
# print('------------------')
# print(locals())

# ------------------------------------------------------

# Дан список внутри которого список из трех чисел. Нужно найти максимальную сумму среди всех списков.
# [[1,2,3], [3,3,5]] -> 6, 11 -> 11

# ls = [[1, 2, 3], [3, 3, 5], [34, 56, 3,4]]

# def find_max(ls):
#     sums = []
#     for x in ls:
#        sums.append(sum(x))
#     return max(sums)

# print(find_max(ls))


# res = max([sum(x) for x in ls]) # comprehention
# print(res)
