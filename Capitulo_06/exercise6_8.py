"""
6.8 – Animais de estimação: Crie vários dicionários, em que o nome de cada dicionário seja o nome de um animal de estimação. Em cada dicionário, inclua o tipo do animal e o nome do dono. Armazene esses dicionários em uma lista chamada pets. Em seguida, percorra sua lista com um laço e, à medida que fizer isso, apresente tudo que você sabe sobre cada animal de estimação.
"""

pets = [
    {
        'lion': {
            'tipo': 'gato',
            'idade': '3 anos'
        }
    },
    {
        'tony': {
            'tipo': 'cachorro',
            'idade': '2 anos'
        }
    },
    {
        'Louro': {
            'tipo': 'papagaio',
            'idade': '5 anos'
        }
    }
]

for pet in pets:
    for name, data in pet.items():
        print(f'Nome: {name.capitalize()}')
        for field, value in data.items():
            print(f'{field.capitalize()}: {value.capitalize()}')
    print()

