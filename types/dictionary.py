# dict() - clovar -> eto uporyadochnaya lektsiya elementov (python 3.7 -> ordered) kajdyi element v slovare soderjitsya v pare klyuch: znacheniye.

# klyuchi doljny byt' unikalnymy i byt' neizmenyaemym tipom dannyh(str, int, tuple etc.)
# togda kak znacheniyzmi mogut vystupat lyubye tipy dannyh.

# thisdict = {
#     'brand' : 'ford',
#     'model' : 'mustung',
#     'year' : 1964
# }

# print(thisdict)
# print(type(thisdict))

# assotsiativnyi massive, hash tables, object(js), structure == dictionory (py)

# dict_ = dict((('key1', 'value'), ('key2', 'value2')))
# print(dict_)
# print(type(dict_))

# --------------------------------------------------------
# user_info = {
#     'first_name' : 'John', 
#     'last_name' : 'Snow', 
#     'age' : 24,
#     'email' : 'johnsnow@gmail', 
#     'role' : 'moderatore',
#     #'first_name' : 'rachel' ---- pereimenovyvaem 
# }
# print(user_info)

# print(user_info.get('age')) # 1-version doesn't snow the  error (none)
# print(user_info['role']) # 2-version

# print(dir({})) information
# item, keys, values

# user_info = {
#      'first_name' : 'John', 
#      'last_name' : 'Snow', 
#      'age' : 24,
#      'email' : 'johnsnow@gmail', 
#      'role' : 'moderatore',      
#  }
# print(user_info.values()) # vyvodit znacheniya
# print(user_info.keys()) # vyvodit klyuch
# print(user_info.items())

# # for value in user_info.values():
#     #print(value)

# for k, v in user_info.items(): # key = k, value = v
#     print('key', k)
#     print('value', v)
#     print()

# a = dict(((1, 2), ('1', '2'))) # kortej
# print(a)
# b = {1: 2, '1': '2'} # dict
# print(b.items())

# for x in b.items():
#     print(x)
#     print(type(x))

# izmeneniye elementtov v slovare
# dict_ = {'name' : 'Jack', 'age' : 23}
# dict_['named'] = 'Johnde' # esli ne naideno to dobavlyaet v spisok
# dict_['name'] = 'John'# pereimenovyvem 
# print(dict_)

# .update() pereimena
# dict_.update({'name' : 'John'})
# print(dict_) # esli net, dobavlyaet 

# fromkeys
# dict_ = {}
# list_ = list(range(1, 200))
# new_dict = dict_.fromkeys(list_, 'value') # 1-key 2-value
# print(new_dict)


# setdefault - rabotaet primerno tak je kak i metod get(), no esli ego net to sozdast novyi klyuch
# dict_ = {'name' : 'Jack', 'age' : 23}
# print(dict_.setdefault('age'))
# # dict_.setdefault('address', 'moskow')
# print(dict_)

# udalenie elementov
# clear(), pop
# pop(key) udalyaet po klyuchu
#  

# dict_ = {'name' : 'Jack', 'age' : 23}
# remove = dict_.pop('age')
# print(dict_)
# print(remove)
# removed = dict_.pop('adderess', 'no such key!')
# print(dict_)
# print(removed)


# popitem() - udalyaet poslednyuyu paru
# dict_ = {'name' : 'Jack', 'age' : 23}
# dict_['address'] = 'kiev str.'

# removed = dict_.popitem()
# print(dict_)
# print(removed)

# ------------------------------------------------

# roles = {
#     0: 'moderator', 
#     1: 'admin', 
#     2: 'customer', 
#     3: 'vendor'
# }

# users = [{

# 'id': 1, 
# 'username':'John', 
# 'role': roles[1]
# }, 
# {'id': '2', 
# 'username' : 'rachey', 
# 'role': roles[1]
# }
# ]

# product = {
#     'id': 1, 
#     'title': 'iphone13',
#     'description':'lorem ipsum', 
#     'price': 200
# }

# print(product)
# id_user = int(input('vvedite vash id: ')) - 1

# print(users[id_user])


# if users[id_user]['role']== roles[1]:
#     choice = input('vvedite chto izmenit\': ')
#     new = input('vvedite new value: ')
#     product.update({choice: new})
# else:
#     raise Exception('permession denied! ')
# print(product)

# /////////////////////////
# 1. Создайте список name_of_friends с именами пяти друзей.
# Затем выведите эти имена по одному, обращаясь к каждому элементу списка. Например:
# name_of_friends = ['hello', 'world', 'python', 'makers', 'bootcamp']

# Результат:
# hello
# world
# python
# makers
# bootcamp
"""
# писать код здесь
# name_of_friends = ('hello', 'world', 'python', ' makers', 'bootcamp')

# for  name_of_friends in name_of_friends:
#   print(name_of_friends)




"""
# 2. Выберите свой любимый вид транспорта (например, мотоциклы или машины) и создайте список labels с марками этого вида транспорта.
# Используя цикл for, выведите утверждения о каждом из элементов списка labels.
# К примеру, если ваш список выглядит так:

#  ['Honda', 'Kawasaki']
# Вывод должен быть:

# I like brand Honda 
# I like brand Kawasaki
"""
# писать код здесь

# brand = ('Honda', 'Kawasaki')
# for brand in brand:
#   print(f' I like brand {brand}')

"""
# 3. Создать список чисел nums.
# Используя цикл и метод списка, запишите все числа меньше 5 в новый список.
# Результат запишите в переменную res и выведите в терминал. nums выглядит так:
# nums = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# результат будет:

# res = [1, 1, 2, 3]

# писать код здесь
# nums = [1, 2, 3, 4, 4, 56, 56564, 45, 4]
# res = []
# for x in nums:
#   if x < 5:
#     res.append(x)
# print(res)
    
"""
# 4. Вместо чисел кратных трём, программа должна печатать 'Fizz'. Вместо чисел кратных пяти - 'Buzz'. Если число кратно и трём, и пяти, программа должна печатать 'FizzBuzz'.
"""
# писать код здесь
# ls = [1, 2, 15, 3, 4, 2, 21, 3, 3, 4]
# for num in ls:
#     if num % 3 == 0:
#         print('Fizz')
#     if num % 5 == 0:
#         print('Buzz')
#     if num % 3 == 0 and num % 5 == 0:
#         print('FillBuzz')




"""
# 5. Создайте пустой список. Напишите программу которая должна 
# записывать в ваш список числа от 0 до 10 включительно. (используйте while)
"""
# писать код здесь
# ls = ()  
# numbers = -1   =0 
# while len(ls) in numbers != -1:     <10 
#   ls.append(numbers)
# print(numbers)
# 
"""
# 6. Вам дан список из чисел. Напишите программу в котором вам необходимо найти факториал каждого числа и записать в новый список.
# list_ = [1,2,3,4,5] 
# формула нахождения факториала - 5! = 1*2*3*4*5 = 120
"""
# писать код здесь
# list_ = [1, 2, 3, 4, 5]
# for i in list_:
#     res = 1
#     while i != 0:
#       res *= i
#       i -=1
#     print(res)
# Rauf's way
# ls = [1, 2, 3, 4, 5]
# res = []
# for num in ls:
#     if num == 1:
#         res.append(1)
#     if num == 2:
#         res.append(1*2)
#     if num == 3:
#         res.append(1*2*3)
#     if num == 4:
#         res.append(1*2*3*4)
#     if num == 5:
#         res.append(1*2*3*4*5)
# print(res)







# 7. Отсортируйте список состоящий и четных и нечетных чисел в переменные а и b. (Например: а = 1, 3, 5, 7  b = 2, 4, 6, 8) Необходимо использовать тернарный оператор.

# # писать код здесь
# num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# a = []
# b = [] 
# for i in num:
#     if i % 2 == 0:
#         a.append(i)
#     if i % 2 != 0:
#         b.append(i)
# print(a)
# print(b)

