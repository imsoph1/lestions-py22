# set() - mnojestvo v python "konteyner", kotoryi soderjit v sebe unikal'nye elementyb v neuporyadochennom vide.
 # {}!!!!
#  a = {} -> mnojestvo {1, 2, 3, 4,5 , 6}
#  b = {1: 'a', 2: 'b',} _> slovary

# set_ = {1, 2, 3, 4, 5, 6, 7, 7, 7}
# # print(set_)

# ls = [1, 2, 'a', False, 2, 3, 2, 4, 5]
# str1 = 'hello world!'
# ls.extend(str1)
# print(ls)

# set_ = set(ls)
# print(set_)
# print(type(set_))

# "*" - raspokovka
# ls = [1, 2,3 ,4 ,5]
# print(*ls) # pasvakovyvaet 
# print(1, 2, 3, 4,5 )

# a = {1, 2, 3, 4, 5}
# print(a)
# print(type(a))
# print(dir(a))

# a.pop()
# print(a)
# fifo(first in first out) - lifo (last in first out)


 #month_user = int(input('Enter month`s number: '))
# if month_user == 1:
    
#  //////////////////////////////////////////////////////
# birth month game
# m = {
#     1 : 'in January', 
#     2 : 'in Fabruary', 
#     3 : 'in March', 
#     4 : 'in April', 
#     5 : 'in May', 
#     6 : 'in June', 
#     7 : 'in July', 
#     8 : 'in August', 
#     9 : 'in September', 
#     10 :'in Noverber', 
#     11 : 'in October', 
#     12 : 'in December'
# } 

# while True:
#     number = input('enter ur birth month: ')
#     if not number.isdigit():
#         print('we need ur real number of month! ')
#         continue
#     number = int(number)
#     if number not in range(1, 13):
#         print('we need ur real number of month! ')
#         continue
#     # print(number)

#     if number in range(3, 6):
#         print(f' you born in {m[number]}. warm season ')
#     elif number in range(6, 9):
#         print(f' you born in {m[number]}. hot season')
#     elif number in range(9, 12):
#         print(f' you born in {m[number]}. cool season')
#     else:
#         print(f' you born in {m[number]}. winter season')

#  second task 

# path = 12
# way = 'dduudduduuud'
# sea = 0 
# valley = 0

# for step in way:
#     if step == 'u':
#         sea += 1
#         if sea == 0:
#             valley += 1
#     elif step == 'd':
#         sea -= 1
# print(f'valley was walked through, {valley} time/times ')
