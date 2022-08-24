'''
CRUD 
C - creat
R - retrieve
U - update
D - delete
'''

# ////////////////////////////////////////

id = 4
date = [
    {'id': 1, 'title':'redmi note 10', 'price': 250, 'description:':'good phone'}, 
    {'id': 2, 'title':'redmi note 9', 'price': 150, 'description': 'cheap phone'}, 
    {'id': 3, 'title':'iphone 13 pro  max', 'price': 1000, 'description':'gerat phone'},
    ]

def get_id():
    id = date[-1]['id']
    id += 1
    return id


def creat_prod():
    product = {
        'id': get_id(), 
        'title': input('enter title of product: '), 
        'price': float(input('enter price of porduct: ')),
        'description' : input('enter description: ')
        }

    date.append(product)
    

def list_of_prod():
    for product in date:
        print('id of product', product['id'])
        print('title:', product['title'])
        print()

def detail_retrieve():
    id_product = int(input('enter id priduct: '))
    try:
        product = list(filter(lambda x: x['id'] == id_product, date))[0]
    
    except IndexError:
        print('there is no such product!')
    else:
        print('id:', product['id'])
        print('title:', product['title'])
        print('desription: ', product['description'])
        print('price: ', product['price'])
        print()

def update_prodact():
    id_product = int(input('enter id product: '))
    flag = False
    try:
        product = list(filter(lambda x: x['id'] == id_product, date))[0]
    except IndexError:
        print('there no such product!')
    else:
        index = date.index(product)
        choice = input('what do u wanna change? (1-title, 2-price, 3-descripton): ')
        if choice == '1':
            date[index]['title'] = input('enter new title: ')
            flag = True
        elif choice == '2':
            date[index]['price'] = input('enter new price: ')
            flag = True
        elif choice == '3':
            date[index]['description'] = input('enter new description: ')
            flag = True
        else:
            print('incorrect choice!! ')
    if flag:
        print('successfully updated!')
    else:
        print('not updated! ')

def delete_product():
    id_product = int(input('enter id product: '))
    flag = False 
    try:
        product = list(filter(lambda x: x['id'] == id_product, date))[0]
    except IndexError:
        print('there no such product!')
    else:
        index = date.index(product)
        date.pop(index)
        flag = True
    if flag:
        print('successfully deleted!')
    else:
        print('not deleted!')


