"""
8.4 – Camisetas grandes: Modifique a função make_shirt() de modo que as
camisetas sejam grandes por default, com uma mensagem Eu amo Python. Crie
uma camiseta grande e outra média com a mensagem default, e uma camiseta
de qualquer tamanho com uma mensagem diferente.
"""

def make_shirt(tamanho='G', mensagem='Eu amo Python'):
    print(f"Tamanho da camiseta: {tamanho}")
    print(f"Frase: {mensagem}")


make_shirt('M', 'Eu sou programador')
print()
make_shirt(mensagem="Python é demais", tamanho='P')
print()
make_shirt()