"""
10.12 – Lembrando o número favorito: Combine os dois programas do Exercício
10.11 em um único arquivo. Se o número já estiver armazenado, informe o
número favorito ao usuário. Caso contrário, pergunte ao usuário qual é o seu
número favorito e armazene-o em um arquivo. Execute o programa duas vezes
para garantir que ele funciona.
"""

import json


filename = 'favorite_number.json'

try:
    with open(filename) as file_object:
        number = json.load(file_object)
except FileNotFoundError:
    number = input('Qual é o seu número favorito?: ')
    with open(filename, 'w') as file_object:
        json.dump(number, file_object)
else:
    print(f"Eu sei qual é o seu número favorito! É {number}")