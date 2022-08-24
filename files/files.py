# Работа с файлами

# Каретка - Указатель - Курсор

# open(<put' do vashego file>)

# file = open('/user/user/Desktop//py.22/files/files.py') # absolute way
# file = open('files.py') # otnositelnyi put'

# print(file)

# rejimy raboty s files 
# 1. r/r+(read)
# 2. w/w+(write)
# 3. a/a+(append)

# file = open('text.txt', 'r')
# print(file.read())
# file.close()

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\
# READ 


# data = file.read()
# print(data)
# print(type(data))
# data = data.split('\n')
# print(data)

# data = file.readline()
# print(data)
# data1 = file.readline(1)
# print(data1)

# data = file.readlines()
# print(data)
# file.close() # we must close oue file

# \\\\\\\\\\\\\\\\\\\\\\\\\\\\
# WRITE(clear and rewrite)


# file = open('text.txt', 'w')
# print(file)
# file.write('hello world!\nmy name is john')
# print(file.tell())
# file.seek(10)
# print(file.tell())
# print(file.read())
# file.close()

# CREAT A NEW FILE

# file = open('text1.txt', 'w')\\\\\\
# print(file)\\\\\\\\\\\
# file.close()\\\\\\\\\\


# with open('text.txt', 'r') as file:
#     data = file.read()
#     print(data)

# ls = ['hello guys!', 'i\'m 23 yo']
# with open('text.txt', 'w') as f:
#     f.writelines(line + '\n' for line in ls)
    
# ---------------------------------------------------------------

# from PIL import Image
# import pytesseract
# import re

# def get_imei_codes(list_images):
#     list_of_imei = []
#     for image in list_images:
#         string = pytesseract.image_to_string(image)
#         print(string)
#         list_of_imei.append(re.findall(r'IME.\d.\s\d+', string))

#     with open('imeicodes.txt', 'w') as file:
#         for x in list_of_imei:
#             for i in x:
#                 file.write(f'{i}\n')


# ls = ['imei.jpg']
# get_imei_codes(ls)
