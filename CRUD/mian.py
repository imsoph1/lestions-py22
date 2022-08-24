from views import *

def main():
    print('hello, for u avalible this functions: \n\tLIST-1\n\tRETRIEVE-2\n\tCREAT-3\n\tUPDATE-4\n\tDELETE-5')
    choice = int(input('enter actios(1, 2, 3, 4, 5): '))
    if choice == 1:
        list_of_prod()
    elif choice == 2:
        detail_retrieve()
    elif choice == 3:
        creat_prod()
    elif choice == 4:
        update_prodact()
    elif choice == 5:
        delete_product()
    else:
        print('invalid choice! ')
    ask = input('do u wanna continue (yes/no)?')
    if ask.lower() == 'yes':
        main()
    else:
        print('bye!')

main()


