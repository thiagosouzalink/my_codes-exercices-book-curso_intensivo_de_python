"""
8.9 – Mágicos: Crie uma lista de nomes de mágicos. Passe a lista para uma
função chamada show_magicians() que exiba o nome de cada mágico da
lista.
"""

def show_magicians(magicians):
    for magician in magicians:
        print(magician)


names_magicians = ['David Copperfield', 'Lance Burton', 'David Blaine', 'Derren Brown']
show_magicians(names_magicians)


