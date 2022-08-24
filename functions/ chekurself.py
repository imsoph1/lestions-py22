# task 1 

# dict_ = {
#     'murat': 24,
#     'erjan': 21,
#     'chyngyz': 24, 
#     'asema': 16
# }

# dict_ = {k:v for k,v in dict_.items() if v > 17}
# print(dict_)

# task 2 

# try:
#     age = int(input('enter ur age: '))
#     if age < 18:
#         raise Exception('vam net 18! ')
# except ValueError:
#     print('vveden nekorrecnyi vozrast! ')
# else:
#     print('sbasibo!')
# finally:
#     print('do svidanii! ')

# task 3 

# fruits = {
#     'apple': 12,
#     'orange': 23,
#     'peach': 46,
#     'banana': 97
# }

# for k, v in list(fruits.items()):
#     if v % 2 == 0:
#         fruits.pop()
# print(fruits)


# task 4 

# number = {
#     'odin': 1, 
#     'dva': 2, 
#     'tri': 3,
#     'chetyre':4
# }

# summa = sum([v for v in number.values()])
# print(summa)

# task 5

# names = {v:v * v for v in range(1, 11) }
# print(names)

# task 6 

# my_dict = {'firts':{'a': 1}, 'second' :{'b': 2}}
# my_dict = {k:v1 for k,v in my_dict.items() for v1 in v.values()}
# print(my_dict)

# task 7
# dict_ = {'just': 1, 'hi': 2, 'guys':3}
# inp = input('enter a key: ')
# try:
#     print(dict_[inp])
# except KeyError:
#     print('net takoga klyucha! ')

# task 8

# try:
#     money = int(input('enter ur money:  '))
#     if money <= 0:
#         raise Exception('u do not have any money! ')
#     else: print(f'you\'ve got money')
#     exit 
# except Exception as e:
#     print(e)
# finally:
#     print('spasibo! ')

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# task 1
