# list()(spisok, massive) - izmenyaemyi posledovatelnyi tip dannyh kotoryi iz sebya predstavlyayet kollektsiyu kakih libo obektov(znacheniye)

# my_list = [1, 'string', False, None, [1,2,3]]
# print(my_list)
# print(type(my_list))

# print(my_list[0])
# print(my_list[-1][0])

# list()
# my_list = list('hello world ')
# print(my_list)
# print(len(my_list))

# tuple_ = ('banana', 'apple', 'cherry')
# print(type(tuple_))
# my_list = list(tuple_)
# print(my_list)
# print(type(my_list))
# range() vozvrachyaet posledovatelnost elementov(chisla)

# ls = list(range(0, 100, 2)) # 3-chislo vybiraet kajdoe * chislo 
# print(ls)
# ////////////////////////////////////////////////////////////////
# ls = list(range(0, 101))
# print(ls)

# for x in ls:
#     # print(x)
#     if x % 2 == 0:
#         print(f'chislo {x} chetnoe, kvadrat {x**2} ')
#     else:
#         print(f'chislo {x} ne chetnoe, kub {x**3} ')

# print(dir(list))
# append(element) - dobovlyaet element v konets spiska

# list_ = [1, 2, 3]
# print(list_)
# list_.append(5)
# list_.append([1, 2, 3])
# print(list_)

# extend(element[iterable]) -> razshirayet spisok dobavlyaya element v konets spiska 

# ls = [1, 2, 3]
# ls.extend([11, 12, 13])
# ls.append([11, 12, 13])
# print(ls)

# insert (<index>, <element> )-> dobavlyaet element po ukazannomu index

# ls = ['string', 2, 3, False]
# ls.insert(1, 1) # v samyi konets ne dobavlyaet (append()) 
# ls.insert(-1, None)
# print(ls)

# index(element, [start], [end]) - vozvrashyaet index elementa v spiske 

# ls = ["hello", 'world', 'my', 'name', 'is', 'sofi', 'queen', 'usa']
# str1 = input('vvedite slovo: ')

# if str1 in ls:
#     print(f'"{str1}" is in list: {ls.index(str1)}')
# else:
#     print('isn\'t ')

# print(ls[ls.index('queen')])


# count(element) -> vozvrachyaet kolichesvto vhojdeniy element v spiske 

# ls = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 5, 5 ]
# result = ls.count(10)
# print(result)

# remove(element) -> udalyaet element, no esli takogo elementa net v spiske to togda vyvoditsya oshibka

# pop([index]) -> udalyaet i vozvrashyaet element po index no esli index ne ukazan to udalyaet posledniy element 

# ls = [5, 1, 2, 3, 4, 5]
# ls.remove(5)
# ls.remove(5)
# print(ls)
# for x in ls:
#     if 5 in ls:
#         ls.remove(5)
# print(ls)

# ls.pop(5)
# print(ls)
# for x in ls:
#     if 5 in ls:
#         ls.pop(la.index(5))
# print(ls)

# deleted = ls.pop()
# print(ls)
# print(deleted)

# sort() -> sortiruet spisok esli v argumentah peredat reserve=True to spisok bedet otsortirovan v ubyvayushem poryadke

# import random 

# ls = []
# for x in range(0, 200):
#     ls.append(random.randint(0, 1000))
# print(ls)


# ls.sort(reverse=True)
# print(ls)

# ls = ['John', 'Deyneris', 'Tirion', 'Ayana', 'Sultan', 'Apple']
# print(ls)
# ls.sort(key=len) # (reverse=True) # po dline
# print(ls)

# for x in ls:
#     print(ord(x[0]))

# ls = [1, 'h', 3]
# ls[1] = 2
# print(ls)

# del ls[-2]
# print(ls)

# pizza = ['first_item', 'second_item', 'third_item', 'forth_item', 'fifth_item', 'sixth_item' ]
# spisok = []

# for x in pizza:
#     if not x.startswith('f'):
#         spisok.append(x)
# print(x)

# 1) nums = [2, 7, 12, 15]
# target = 9
# 0, 1

# 2) nums = [4,11,2,5,1,6]
# target = 8
# 2 5 

# nums = [4,11,2,5,1,6]
# target = 8

# for i in range(0, len(nums)):
#     num = target - nums[i]
#     if num in nums:
#         if num == nums[i]:
#             continue
#         k = nums.index(num)
#         print(f'otvet: {i} {k}')
#         break


# for i in range(1, 8):
#     input('vvedite chisla: ')



