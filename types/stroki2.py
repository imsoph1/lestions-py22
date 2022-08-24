# print(dir(str))

# replace(old, new, [count]) - меняет в строке old на new значениеб если вы укажете count, то он заменит count раз.

# text = 'ha ha ha ha '
# print(text[::-1])
# result = text.replace('a', 'i', 2)
# print(result)
# print(text)
# str1 = 'hello world! My name is Sofi!'
# print(str1.replace('Sofi', 'me'))

# strip() - убирает пробельные символы в начале и в конце строке.
# rsrip, lstrip

# text = input('enter the text')
# print(text)
# result = text.strip()
# print(result)

# text = '   hello   '
# print(len(text))
# result = text.rstrip()
# print(result)
# print(len(result))

# startswith(string, [start], [end]) - возвращает true если строка начинается с string, иначе False

# text = 'hello wolrd'
# print(text.startswith('w'))
# print(text.startswith('h'))
# print(text.startswith('hello'))
# print(text.startswith('d', -1))
# print(text.startswith('hello'))
# # -------------------
# print(id('h'))
# print(id('H'))
# # -------------------

# print(dir(str))
#****************
# isalpha() - проверяет состоит ли наша строка из символов (из лат алф или кирилицы) 
# isdigit()  - состоит ли строка полностью из чисел
# isalnum() - показывает, состоит ли из строк и чисел
#*************
# text = 'привет'
# print(text.isalpha())

#////////////////////////////////////
# text = 'l5'
# print(text.isdigit())
# print(text.isnumeric())

# isdigit()
# islower()
# issupper()
# istitle()
# isalpha()

# index(value, [start], [end], ) - выводит индекс значения value в нашей строке. 

# text = 'hello world! My name is John'
# result = text.find('p')
# print(result)

# rindex - поиск с конца

# find(value, [start], [end]) - делает тоже самое что и метод index. Разница в том что, если value не найден, то возвращается -1 
# rfind

# text = 'hello'
# print(text.find('l'))

# count ('string') - считает количество вхождений string в нашу строку

# text = 'hello world i\'m from bishkek'
# result = text.count('o')
# print(result)


# swapcase() - возвращает строчку в которой каждая буква будет иметь противоположный регистр
# lower(), upper()

# text = 'Hello World'
# print(text.swapcase())
# print(text.lower())
# print(text.upper())

#capitalize() - переводит первую букву в верхний регистр

# print('hello'.capitalize())

# print(input('vvedite vashe imya:').capitalize().istitle())

# title - переводит символы в верхний регистр 

# text = 'john, jery, nurs'
# print(text.title())
# print(text.capitalize())

# split() - дробит строчке по разделителю который находится в строке. Разделяет строчку и возвращает строку и возвращает тип данных list

# justme = "hello i\'m here i came to visit u guys!".split()
# text = " * ".join(justme)
# print(text)

# join(iterable) -  соединяет строки которые находится в iterable по раздилителю

# sentence = ' | '.join(ls)
# print(sentence)
# sentence = ' | '.join(ls)
# print(sentence)

#////////////////////////////////////////
# word = 'hello'
# result = word[-1] + word[1:-1] + word[0]
# print(result)

# word = 'John'
# result = f'{word[-1:]}{word[1:-1]}{word[:1]}'
# print(result)

