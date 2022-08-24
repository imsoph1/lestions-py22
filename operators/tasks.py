import random

ls = ['plov', 'Manty', 'Lagman', 'Kuurdak', 'Pelmeni' ]

pl = 0
m = 0
l = 0
k = 0
p = 0

for x in range(0, 1000000):
    choice = random.choice(ls)
    print(choice)
    if choice.lower() == 'plov':
        pl = pl + 1
    elif choice.lower() == 'manty':
        m += 1
    elif choice.lower() == 'kuurdak':
        k += 1
    elif choice.lower() == 'lagman':
        l +=1
    elif choice.lower() == 'pelmen':
        p +=1
        
        
print(f'Plov={pl}. Manty={m}. Kuurdak={k}. Lagman={l}. Pelmen={pl}')


