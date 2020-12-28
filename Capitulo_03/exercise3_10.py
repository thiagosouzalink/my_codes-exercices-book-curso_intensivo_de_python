"""
3.10 – Todas as funções: Pensa em algo que você poderia armazenar em uma lista. Por exemplo, você poderia criar uma lista de montanhas, rios, países, cidades, idiomas ou qualquer outro item que quiser. Escreva um programa que crie uma lista contendo esses itens e então utilize cada função apresentada neste capítulo pelo menos uma vez.
"""


# Funções apresentadas até este exercício.
# list.append(), list.insert(), del list[index], list.pop(), list.remove()
# list.sort(), sorted(list), list.reverse(), len(list)

cidades = ["São Paulo", "Belém", "Rio de Janeiro", "Florianópolis", "Recide"]
print(cidades)

cidades.append("Manaus")
print(cidades)

cidades.insert(3, "Salvador")
print(cidades)

del cidades[2]
print(cidades)

cidades.pop()
print(cidades)

cidades.remove("Florianópolis")
print(cidades)

print(sorted(cidades))
print(cidades)

cidades.reverse()
print(cidades)

cidades.sort()
print(cidades)

print(len(cidades))