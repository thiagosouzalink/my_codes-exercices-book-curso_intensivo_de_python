"""
6.7 – Pessoas: Comece com o programa que você escreveu no Exercício 6.1 (página 147). Crie dois novos dicionários que representem pessoas diferentes e armazene os três dicionários em uma lista chamada people. Percorra sua lista de pessoas com um laço. À medida que percorrer a lista, apresente tudo que você sabe sobre cada pessoa.
"""

people = [
    {'first_name': 'Thiago', 'last_name': 'Souza', 'age': 31, 'city': 'Ananindeua'},
    {'first_name': 'Kaleb', 'last_name': 'Guimarães', 'age': 16, 'city': 'Ananindeua'},
    {'first_name': 'Cristiano', 'last_name': 'Ronaldo', 'age': 35, 'city': 'Turim'}
]

for person in people:
    for field, value in person.items():
        print(f"{field.capitalize()}: {value}")
    print()