"""
10.8 – Gatos e cachorros: Crie dois arquivos, cats.txt e dogs.txt. Armazene pelo
menos três nomes de gatos no primeiro arquivo e três nomes de cachorro no
segundo arquivo. Escreva um programa que tente ler esses arquivos e mostre o
conteúdo do arquivo na tela. Coloque seu código em um bloco try-except
para capturar o erro FileNotFound e apresente uma mensagem simpática caso
o arquivo não esteja presente. Mova um dos arquivos para um local diferente
de seu sistema e garanta que o código no bloco except seja executado de
forma apropriada.
"""
file_cats = 'cats.txt'
file_dogs = 'dogs.txt'
try:
    with open(file_cats) as file_object:
        names_cats = file_object.readlines()
except FileNotFoundError:
    print(f'Desculpe, o arquivo {file_cats} não foi encontrado.')
else:
    print('\nOs nomes dos gatos são:')
    for cat in names_cats:
        print(cat.strip())
    print()

try:
    with open(file_dogs) as file_object:
        names_dogs = file_object.readlines()
except FileNotFoundError:
    print(f'Desculpe, o arquivo {file_dogs} não foi encontrado.')
else:
    print('Os nomes dos cachorros são:')
    for dog in names_dogs:
        print(dog.strip())
    print()