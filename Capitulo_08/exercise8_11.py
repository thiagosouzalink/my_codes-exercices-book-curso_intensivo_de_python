"""
8.11 – Mágicos inalterados: Comece com o trabalho feito no Exercício 8.10.
Chame a função make_great() com uma cópia da lista de nomes de mágicos.
Como a lista original não será alterada, devolva a nova lista e armazene-a em
uma lista separada. Chame show_magicians() com cada lista para mostrar que
você tem uma lista de nomes originais e uma lista com a expressão o Grande
adicionada ao nome de cada mágico.
"""

def make_great(magicians):
    for i in range(0, len(magicians)):
        magicians[i] = f'O Grande {magicians[i]}'
    return magicians

def show_magicians(magicians):
    for magician in magicians:
        print(magician)


names_magicians = ['David Copperfield', 'Lance Burton', 'David Blaine', 'Derren Brown']

names_magicians_changed = make_great(names_magicians[:])

show_magicians(names_magicians)
print()
show_magicians(names_magicians_changed)