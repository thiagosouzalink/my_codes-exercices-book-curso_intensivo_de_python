"""
10.7 – Calculadora para adição: Coloque o código do Exercício 10.6 em um
laço while para que o usuário possa continuar fornecendo números, mesmo se
cometerem um erro e digitarem um texto no lugar de um número.
"""
while True:
    n1 = input('Digite o valor do primeiro número: ')
    n2 = input('Digite o valor do segundo número: ')

    try:
        n1 = int(n1)
        n2 = int(n2)
    except ValueError:
        print('Você não digitou número(s) inteiro(s).')
    else:
        print(f'A soma é: {n1+n2}')
        break