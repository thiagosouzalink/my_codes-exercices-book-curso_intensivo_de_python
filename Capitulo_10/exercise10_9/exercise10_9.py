"""
10.9 – Gatos e cachorros silenciosos: Modifique o seu bloco except do Exercício
10.8 para falhar silenciosamente caso um dos arquivos esteja ausente.
"""

file_cats = 'cats.txt'
file_dogs = 'dogs.txt'
try:
    with open(file_cats) as file_object:
        names_cats = file_object.readlines()
except FileNotFoundError:
    pass
else:
    print('\nOs nomes dos gatos são:')
    for cat in names_cats:
        print(cat.strip())
    print()

try:
    with open(file_dogs) as file_object:
        names_dogs = file_object.readlines()
except FileNotFoundError:
    pass
else:
    print('Os nomes dos cachorros são:')
    for dog in names_dogs:
        print(dog.strip())
    print()