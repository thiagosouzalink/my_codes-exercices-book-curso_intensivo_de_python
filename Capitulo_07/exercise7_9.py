"""
7.9 – Sem pastrami: Usando a lista sandwich_orders do Exercício 7.8, garanta
que o sanduíche de 'pastrami' apareça na lista pelo menos três vezes.
Acrescente um código próximo ao início de seu programa para exibir uma
mensagem informando que a lanchonete está sem pastrami e, então, use um
laço while para remover todas as ocorrências de 'pastrami' e
sandwich_orders. Garanta que nenhum sanduíche de pastrami acabe em
finished_sandwiches.
"""

sandwich_orders = ["Hambúrguer", "Pastrami", "Big Mac", "Pastrami", "Bauru", "Pastrami", "Misto", "Americano"]
finished_sandwiches = []

print("Estamos sem saunduíche do tipo Pastrami\n")
while "Pastrami" in sandwich_orders:
    sandwich_orders.remove("Pastrami")

while sandwich_orders:
    sandwich = sandwich_orders.pop()
    print(f"Preparei seu {sandwich}")
    finished_sandwiches.append(sandwich)
print("\nSanduíches preparados:")
for sandwich in finished_sandwiches:
    print('  ',sandwich)