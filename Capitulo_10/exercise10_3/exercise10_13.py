"""
10.3 – Convidado: Escreva um programa que pergunte o nome ao usuário.
Quando ele responder, escreva o nome em um arquivo chamado guest.txt.
"""

name = input('Digite seu nome: ').strip()

with open('guest.txt', 'w', encoding='UTF-8') as file_object:
    file_object.write(name)