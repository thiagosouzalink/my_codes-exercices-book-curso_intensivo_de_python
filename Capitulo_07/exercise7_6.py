"""
7.6 – Três saídas: Escreva versões diferentes do Exercício 7.4 ou do Exercício
7.5 que faça o seguinte, pelo menos uma vez: • use um teste condicional na
instrução while para encerrar o laço; • use uma variável active para controlar
o tempo que o laço executará; • use uma instrução break para sair do laço
quando o usuário fornecer o valor 'quit'.
"""

# Exercício 7.5
# # Versão 1
# idade = 0
# while idade >= 0:
#     idade = int(input("Digite sua idade (-1 para sair): "))
#     if idade >= 0:
#         if idade < 3:
#             print("Seu ingresso é gratuito\n")
#         elif idade <= 12:
#             print("Seu ingresso custa 10 dólares\n")
#         else:
#             print("Seu ingresso custa 15 dólares\n")
#     else:
#         print("\nObrigado!")

# Versão 2
# active = True
# while active:
#     idade = int(input("Digite sua idade (-1 para sair): "))
#     if idade < 0:
#         active = False
#         continue
#     else:
#         if idade < 3:
#             print("Seu ingresso é gratuito\n")
#         elif idade <= 12:
#             print("Seu ingresso custa 10 dólares\n")
#         else:
#             print("Seu ingresso custa 15 dólares\n")
# print("\nObrigado!")

# Versão 3
while True:
    idade = input("Digite sua idade ('quit' para sair): ")
    if idade == "quit":
        print("\nObrigado!")
        break
    idade = int(idade)
    if idade < 0:
        print("Ops, você digitou uma idade negativa, tente novamente...")
        continue
    if idade < 3:
        print("Seu ingresso é gratuito\n")
    elif idade <= 12:
        print("Seu ingresso custa 10 dólares\n")
    else:
        print("Seu ingresso custa 15 dólares\n")