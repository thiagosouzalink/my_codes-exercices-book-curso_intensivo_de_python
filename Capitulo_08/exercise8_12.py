"""
8.12 – Sanduíches: Escreva uma função que aceite uma lista de itens que uma
pessoa quer em um sanduíche. A função deve ter um parâmetro que agrupe
tantos itens quantos forem fornecidos pela chamada da função e deve
apresentar um resumo do sanduíche pedido. Chame a função três vezes usando
um número diferente de argumentos a cada vez.
"""

def items_sandwich(*items):
    if items:
        print('\nItens pedidos para o sanduíche: ')
        for item in items:
            print(item.capitalize())
    else:
        print('\nNenhum item foi pedido para o sanduíche')

items_sandwich('Queijo', 'Tomate', 'Bacon')
items_sandwich('alface', 'batata')
items_sandwich()