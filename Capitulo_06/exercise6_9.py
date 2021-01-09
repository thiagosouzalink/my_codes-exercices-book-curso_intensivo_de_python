"""
6.9 – Lugares favoritos: Crie um dicionário chamado favorite_places. Pense em três nomes para usar como chaves do dicionário e armazene de um a três lugares favoritos para cada pessoa. Para deixar este exercício um pouco mais interessante, peça a alguns amigos que nomeiem alguns de seus lugares favoritos. Percorra o dicionário com um laço e apresente o nome de cada pessoa e seus lugares favoritos.
"""

favorite_places = {
    'thiago': {'places': ['Amsterdã', 'Milão', 'Paris']},
    'paulo': {'places': ['Tokyo', 'Londres', 'Nova York']},
    'mateus': {'places': ['São Paulo', 'Madri', 'Berlim']}
}

for name, places in favorite_places.items():
    print(f'Nome: {name.capitalize()}')
    for lista in places.values():
        print('Lugares favoritos: ', end='')
        for place in lista:
            print(place, end=' ')
        print()
    print()

