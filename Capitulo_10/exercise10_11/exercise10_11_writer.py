"""
10.11 – Número favorito: Escreva um programa que pergunte qual é o número
favorito de um usuário. Use json.dump() para armazenar esse número em um
arquivo. Escreva um programa separado que leia esse valor e apresente a
mensagem “Eu sei qual é o seu número favorito! É _____.”.
"""
import json


number = input('Qual é o seu núemro favorito?: ')

filename = 'favorite_number.json'

try:
    number = int(number)
except ValueError:
    print('Você não digitou um núemro inteiro.')
else:
    with open(filename, 'w') as file_object:
        json.dump(number, file_object)