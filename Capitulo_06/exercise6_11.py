"""
6.11 – Cidades: Crie um dicionário chamado cities. Use os nomes de três cidades como chaves em seu dicionário. Crie um dicionário com informações sobre cada cidade e inclua o país em que a cidade está localizada, a população aproximada e um fato sobre essa cidade. As chaves do dicionário de cada cidade devem ser algo como country, population e fact. Apresente o nome de cada cidade e todas as informações que você armazenou sobre ela.
"""

cities = {
    'amsterda': {
        'pais': 'Holanda',
        'populacao': '833 989 habitantes',
        'curiosidade': 'Conhecida por seu patrimônio artístico.'    
    },
    'paris': {
        'pais': 'França',
        'populacao': '2 148 271 habitantes',
        'curiosidade': 'Conhecida como a cidade da luz.'
    },
    'rio de janeiro': {
        'pais': 'Brasil',
        'populacao': '6 719 000 habitantes',
        'curiosidade': 'Conhecida como a cidade maravilhosa'
    },
}

for city, data in cities.items():
    print(f'Cidade: {city.title()}')
    for field, value in data.items():
        print(f'{field.capitalize()}: {value}')
    print()

   