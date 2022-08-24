# функция  - это изменяемая часть программы, которая может  вызывать в других частях програмы столько раз сколько угодно.

# def name_of_function(<a b> #parametry ):
    #<body> #kod, какая та логика которая возвращает конечный результат
#   <resultat> # operator dlya vozvrasheniya resultata

# name_of_function(5, 6 #argumenty)

#parametry funktsii  -  переменные которые будет принимать наша функция для того чтобы мы могли работать с даннымы которые передаются в нашу функция 

# return = оператор который нужен для того чтобы функция возвращает результат. Если return не указать то функция возвращает None

# a = print('hello')
# print(a)

# a = max(range(1, 100))
# print(a)     

# def our_len(a): # peremetr
#     i = 0
#     for x in a:
#         i += 1
#     return i 

# ls = [1, 2, 3, 4, 5]
# str1 = 'hello guys'
# print(our_len(str1))  # argument

# # funksiya s malenkoi bukvoi!

# def sumTwoNums(num1, num2): # parametry
#     result = num1 + num2
#     print(result)

# a = sumTwoNums(5, 15) # arguments
# print(a)

# def isEven(num):
#     if num % 2 == 0:
#         return True
#     print('hello')
#     return False # instead of else: # after return does not show any cod

# a = 10
# b = int(input('vvedite  chislo: '))


# print(isEven(6))
# print(isEven(a))
# print(isEven(b))

# def isEven(num: int) -> bool:
#     'our fuctioin returns True or False while cheking number for an even number '
#     if num % 2 == 0:
#         return True 
#     return False

# print(isEven(6))
# isEven
# dir

# anna, ded, kabak. kazak # polindrom
# from typing import List

# def get_polindrom(words: List[str]) -> List[str]:
#     'function return a polindrom string list'
#     result = []
#     for x in words:
#         if x.lower() == x[::-1].lower():
#             result.append(x)
#     return result

# some_words = ['john', 'ono', 'anna', 'ded', 'kabak', 'kazak']
# print(get_polindrom(some_words))
# print(get_polindrom(['john', 'jemie', 'kyrgyzstan', 'apa']))

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# def get_procentage(money: float, period: int) -> float:
#     'return final amount of money'
#     if money < 30000:
#         raise Exception('vy vveli nekorreknyi srok deneg! min stavka 30 000 somov!')
#     if period < 3:
#         raise Exception('vy vveli nekorreknyi srok dlya depozita! min srok  3 goda!')

#     i = 0
#     while i < period:
#         money += money * 0.1
#         # money  = money * 1.1
#         # money + (money / 100 * 10 )
#         i += 1
#     return money
    
# money = float(input('vvedite summu deneg: '))
# year = int(input('vvedite srok vashego deposita: '))
# print(get_procentage(money, year))

# default parametry

# def func():
#   print()


# def print_welcom(name = 'user'):
#     print(f'welcom, {name}!')
# print_welcom('john')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\


# def introduce(name, lastname, work=None):
#     print(f'this person\'s name is {name}')
#     print(f'this person\'s last name is {lastname}')
#     if work:
#         print(f'this person\'s job is {work}')
# introduce('john', 'Snow', 'teacher')

#\\\\\\\\\\\\\\\\\\\\\\\\\\\

# def get_reverse_string(text):
#     spisok = text.split()
#     #print(spisok)
#     return ' '.join(spisok[::-1])

# get_reverse_string('hello world john snow nice to meet u!')
# print(get_reverse_string('hello world john snow nice to meet u!'))
