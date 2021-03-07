"""
10.6 – Adição: Um problema comum quando pedir entradas numéricas ocorre
quando as pessoas fornecem texto no lugar de números. Ao tentar converter a
entrada para um int, você obterá um TypeError. Escreva um programa que
peça dois números ao usuário. Some-os e mostre o resultado. Capture o
TypeError caso algum dos valores de entrada não seja um número e apresente
uma mensagem de erro simpática. Teste seu programa fornecendo dois números
e, em seguida, digite um texto no lugar de um número.
"""

n1 = input('Digite o valor do primeiro número: ')
n2 = input('Digite o valor do segundo número: ')

try:
    n1 = int(n1)
    n2 = int(n2)
except ValueError:
    print('Você não digitou número(s) inteiro(s).')
else:
    print(f'A soma é: {n1+n2}')