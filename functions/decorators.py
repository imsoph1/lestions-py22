# Функция высшего порядка - это функция, которая в качестве аргумента принимает другую функцию

# Декоратор - это функция, которая позволяет без изменения кода вернуть другую функцию для того, чтобы расширить функционал обернутой функции

# def decorator(func):
#     print(func)
#     return func()

# def hello():
#     print('Ya hello :)')
#     return 'Hello'

# def john():
#     print('Ya john')
#     return 'John'

# print(hello())
# print()
# print(decorator(hello))
# print()
# print(decorator(john))


# def benchmark(func):
#     import time
#     start = time.time()
#     func()
#     finish = time.time()
#     print(f'Время выполнения функции {func.name}, заняло: {finish-start}')

# def loop():
#     i = 0
#     range_number = 1000000
#     while i <= range_number:
#         print(i)
#         i += 1

# benchmark(loop)


# Pythonic way -> @benchmark
    # Синтаксический сахар - это красота кода

# def benchmark(func):
#     def wrapper():
#         import time
#         start = time.time()
#         func()
#         finish = time.time()
#         print(f'Время выполнения функции {func.name}, заняло: {finish-start}')
#     return(wrapper)

# @benchmark
# def loop():
#     i = 0
#     range_number = 100000
#     while i <= range_number:
#         # print(i)
#         i += 1

# @benchmark
# def add():
#     range_number = 100000
#     ls = []
#     for i in range(0, range_number):
#         ls.append(i)

# loop()
# add()


# def strong(func):
#     def wrapper(*args, **kwargs):
#         return '<strong>' + func() + '</strong>'
#     return wrapper

# def div(func):
#     def wrapper(*args, **kwargs):
#         return '<div>' + func() + '</div>'
#     return wrapper

# @div
# @strong
# @div
# def get():
#     return 'John Snow'

# print(get())

