"""
8.10 – Grandes mágicos: Comece com uma cópia de seu programa do
Exercício 8.9. Escreva uma função chamada make_great() que modifique a
lista de mágicos acrescentando a expressão o Grande ao nome de cada
mágico. Chame show_magicians() para ver se a lista foi realmente modificada.
"""

def make_great(magicians):
    for i in range(0, len(magicians)):
        magicians[i] = f'O Grande {magicians[i]}'

def show_magicians(magicians):
    for magician in magicians:
        print(magician)


names_magicians = ['David Copperfield', 'Lance Burton', 'David Blaine', 'Derren Brown']
make_great(names_magicians)
show_magicians(names_magicians)
