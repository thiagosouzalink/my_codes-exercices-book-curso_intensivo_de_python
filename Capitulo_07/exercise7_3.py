"""
7.3 – Múltiplos de dez: Peça um número ao usuário e, em seguida, informe se o
número é múltiplo de dez ou não.
"""

numero = int(input("Digite o valor de um número: "))

if numero % 10 == 0:
    print(f"O número digitado {numero} é múltiplo de 10")
else:
    print(f"O número digitado {numero} não é múltiplo de 10")