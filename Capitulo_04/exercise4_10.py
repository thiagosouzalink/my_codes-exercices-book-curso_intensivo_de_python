"""
4.10 – Fatias: Usando um dos programas que você escreveu neste capítulo, acrescente várias linhas no final do programa que façam o seguinte: 
• Exiba a mensagem Os três primeiros itens da lista são: Em seguida, use uma fatia para exibir os três primeiros itens da lista desse programa.
• Exiba a mensagem Três itens do meio da lista são:. Use uma fatia para exibir três itens do meio da lista.
• Exiba a mensagem Os três últimos itens da lista são:. Use uma fatia para exibir os três últimos itens da lista.
"""

# Criando uma lista com valores no intervalo [1, 20]
numeros = list(range(1, 21)) 

print(f"Os três primeiros itens da lista são: {numeros[0:3]}")
print(f"Três itens do meio da lista são: {numeros[8:11]}")
print(f"Os três últimos itens da lista são: {numeros[-3:]}")