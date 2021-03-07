import json


filename = 'favorite_number.json'

try:
    with open(filename) as file_object:
        number = json.load(file_object)
except FileNotFoundError:
    print(f'O arquivo {filename} não existe.')
else:
    print(f"Eu sei qual é o seu número favorito! É {number}")