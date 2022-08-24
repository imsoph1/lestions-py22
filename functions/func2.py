# def sum_of_args(a, b, c, d): #a, b, c, d parametry
#     return a + b + c + d

# result = sum_of_args
# print(result)
# print(type(result))
# print(result(5, 10 , 12, 7))

# -------------------------------------------------------------
# позиционные и именнованные аргументы

# def printParams(a = None, b = None, c = None):
#     print(a, 'is stored in param a')
#     print(b, 'is stored in param b')
#     print(c, 'is stored in param c')


# printParams(b = 1, c = 2) # передается по позициям \ изменяемые и позиционные параметры

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\

# def sum_of_args(a, b, c, d): # параметры
#     return a + b + c + d

# print(sum_of_args(5, 10, 15, 20)) # аргументы (required) (позиционные аргументы)
# print(sum_of_args(a = 5, b = 10, c = 15, d = 20 )) # keyword arg(именнованные аргументы)
# print(sum_of_args(10, 50, d = 50, c = 100))

# ''''''''''''''''''''''''''''''''
# operatop *

# a = [1, 2, 3]
# b = [4, 5, 6]
# c = [*a, b] # c = [*a, *b]
# print(c)
# print(a)
# print(*a)

#*args, **kwars v function
# def printScores(student, *args): # args -> tuple
#     print(f' students\'s name: {student}')
#     # print(args)
#     # print(type(args))
#     for i in args:
#         print('score', i)
# printScores('john', 1, 2, 3, 4, 5 ,67,8)

# kwargs

# def print_pet_names(owner, **pets):
#     print(f'owner name: {owner}')
#     # print(pets)
#     # print(type(pets))
#     for pet, name in pets.items():
#         if type(name) is list:
#             print(f'{pet}:', *name)
#         else:
#             print(f'{pet}: {name}')

# print_pet_names('john snow', dog = 'rex', cat = 'lavy', fish = ['nemo', 'dory', 'alex'], turtle = 'leonardo') # kwargs -> dictionary 


# \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
# def get_some_data(a, b, *args, **kwargs):
#     print('parametry a i b:', a, b)
#     print('argumenty:', args)
#     print('imenovannye argumenty:', kwargs)
#     print(args[0])
#     print(args[-1])
#     print(kwargs['name'])

# get_some_data(1, 2, 3, 4, 5, lang='pythin', name = 'john snow', car = 'bwm m8')

# -------------------------------------------------------------------------------------------------

# def generator_random_string(len_):
#     import string as s
#     import random 
#     random_str = ''.join(random.choice(s.ascii_lowercase + s.ascii_lowercase + s.digits) for i in range(0, len_))
#     return random_str

# print(generator_random_string(15))
   
# ---------------------------------------------------

# def add(a, b): 
#     return a + b
# def subtract(a, b): 
#     return a - b
# def multiply(a, b): 
#     return a * b
# def divide(a, b):
#     try:
#         return a / b
#     except ZeroDivisionError:
#         return 'На ноль делить нельзя!'
# def calc(num1, num2):
#     operator = input('Введите оператор(+, -, *, /): ')
#     if operator == '+': return add(num1, num2)
#     elif operator == '-': return subtract(num1, num2)
#     elif operator == '*': return multiply(num1, num2)
#     elif operator == '/': return divide(num1, num2)
#     else: return('Вы ввели неверный оператор!')
# def main():
#     try:
#         num1 = float(input('Введите первое число:'))
#         num2 = float(input('Введите второе число:'))
#     except ValueError:
#         print('Вы ввели некорректное число!')
#         main()
#         return
#     while True:
#         result = calc(num1, num2)
#         if type(result) != float:
#             print(f'Result: {result}')
#         else:
#             print(f'Result: {result}')
#             break
    
#     question = input('Хотите продолжить?(Yes/ No): ')
#     if question.lower() == 'yes':
#         main()
#     else:
#         print('Спасибо за использование нашего калькулятора! ПОКА!')
# main()
