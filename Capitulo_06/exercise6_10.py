"""
6.10 – Números favoritos: Modifique o seu programa do Exercício 6.2 (página 147) para que cada pessoa possa ter mais de um número favorito. Em seguida, apresente o nome de cada pessoa, juntamente com seus números favoritos.
"""

pessoas = {
    'thiago': [10, 23, 5],
    'jessica': [4, 11, 6],
    'paulo': [5, 20],
    'juliane': [8, 1, 13, 6],
    'viviane': [5, 27],
}

for nome, numeros in pessoas.items():
    print(f"Nome: {nome.capitalize()}\t Número(s) favorito(s): ", end='')
    for numero in numeros:
        print(numero, end=' ')
    print()

