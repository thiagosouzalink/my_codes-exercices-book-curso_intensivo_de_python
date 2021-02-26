"""
8.3 – Camiseta: Escreva uma função chamada make_shirt() que aceite um
tamanho e o texto de uma mensagem que deverá ser estampada na camiseta.
A função deve exibir uma frase que mostre o tamanho da camiseta e a
mensagem estampada.
"""

def make_shirt(tamanho, texto):
    print(f"Tamanho da camiseta: {tamanho}")
    print(f"Frase: {texto}")


make_shirt('M', 'Eu amo Python')
print()
make_shirt(texto="Python é demais", tamanho='P')