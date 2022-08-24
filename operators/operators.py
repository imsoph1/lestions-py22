# operatory sravnenie
# uslovnye operatory 
# logicheskie operatory

# operatop sravnenie
# n<, >, ==(ravno), <=, >=, !=(ne ravno)

# num1 = 18
# num2 = 15
# print(18 > 15)

# stroka1 = 'hello'
# stroka2 = 'world'
# print(stroka1  < stroka2 )
# print(ord('H'))
# print(ord('W'))

# text = 'hello world'
# for letter in text:
#     print(ord(letter))

# print(chr(1080))

# uslovnye operatory
# if
# elif
# else

# if <condition>:
#     <body if>
#     <body if> #srabotaet esli v if pridet true

# elif <condition> : 
#     <body elif>
# elif <condition>:
#     <body elif>
# elif:
#     <body< #srabotaet esli vo vseh usloviyah prishlo false

# string = input('enter something: ')

# if string == 'hello':
#     print('hello stranger!')
# elif string == 'John':
#     print('wellcome back John Snow')
# elif string == 'mercedes':
#     print('mercedes benz s class! ')
# else:
#     print('sovpadenie ne naideno')

# print("kod zakonchilsya!")

# from random import random


# email = input('enter email: ')
# password1 = input('enter password: ')

# if len(password1) <8:
#     raise Exception('too short password !')
# password2 = input('enter password confirmation: ')

# if password1 != password2:
#     raise Exception('password didn\'t match')
# else:
#     print('successfully signed up! ')

# age = input('enter ur age: ')

# if age.isdigit():
#     age = int(age)
# else:
#     raise ValueError('enter correct values!! ')

# if age < 18:
#     print(f'Chuvak prihodi cherez {18 - age} goda/let!!!')
# else:
#     print('vy podhodite po vozrastu! ')


# password = input('enter ur password: ')

# symbols = ['_', ',', '.', '%', '#', '@', '+', '-', '(', ')']

# nums = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

# flag = False
# for element in symbols:
#     if element in password:
#         flag = True

# flag_nums = False 
# for num in ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']:
#     if num in password:
#         flag_nums = True

# if not flag_nums:
#     raise Exception('vy vveli tolko bukvy, nujny eshe tsifry! ')
# elif password.isdigit():
#     raise Exception('vy vveli tolko tsifry nujny eche bukvy')
# elif not flag:
#     raise Exception('vy ne vveli hotya by odin cpets simvol v porol!!(_,.()*...)')
# else:
#     print('vy vveli korreknyi porol!')

#logincheskie operatory
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# and -> logincheskoe 'i'
# or -> log ilshift
# not -> log otritsaniye

# operatory identificatsiyii
# in -> properyayet nalichiye elementa vnutri kakogo libo massiva ili stroki
# is -> sravnivaet yacheikiu pamyati dvuh elementa 
# == -> sravnivaet po znacheniye 
# is not -> otritsatelnoe sravneniya yacheek pamyati

# my_age = 20
# ur_age = 19
# result = my_age == 22 and ur_age ==19
# print(result)

# result = my_age > 18 or ur_age < 17
# print(result)

# result = not my_age > 25 
# print(result)

# is_google_user = True
# is_github_user = True
# is_age_greater_21 = False
# user_coins = 3000


# if (is_google_user and is_github_user) and (is_age_greater_21 or user_coins > 5000):
#     print('you can enter the system mr John Snow!')
# else: 
#     print('sorry u coudn\'t enter!')

# str1 = 'hello world'
# choice = input('vvidite simvol: ')

# if choice in str1:
#     print(f'simvol {choice} yest v stroke: "{str1}" ')
# else:
#     print(f'simvola {choice} net v stroke: "{str1}" ')

#dano [1--100]
# \3 -> <3> - fu
# \5 -> <5> - ba
# \3, \5 -> <15> - fuba

# for number in range(1,100):
#     if number % 3 == 0 and number % 5 ==0:
#         print(f'{number} +fuba')
#     elif number % 5 ==0:
#         print(f'{number} +ba')
#     elif number % 3 ==0:
#         print(f'{number} +fu')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# num = 1
# while num >= 0:
#     num = int(input('vvedite chislo: '))
#     if num < 0 :
#         print('otritsatelnoe chislo! ')
        # inkrement


# task culculate

# f_num = int(input('Введите первое число: '))
# s_num = int(input('Введите второе число: '))

# operation = input("Выберите операцию из следующих: +, -, *, /, %, **, //:")

# if operation == "+":
#         print(f_num + s_num)
# elif operation == "-":
#         print(f_num - s_num)
# elif operation == "*":
#         print(f_num * s_num)
# elif operation == "/":
#         print(f_num / s_num)
# elif operation =="%":
#         print(f_num % s_num)
# elif operation == "**":
#         print(f_num ** s_num)
# elif operation == "//":
#         print(f_num // s_num)
# else:
#         raise ValueError('Данной операции нет в системе')

# mini game

