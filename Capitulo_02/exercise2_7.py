"""
2.7 – Removendo caracteres em branco de nomes: Armazene o nome de uma pessoa e inclua alguns caracteres em branco no início e no final do nome. Lembre-se de usar cada combinação de caracteres, "\t" e "\n", pelo menos uma vez.
"""

nome = " \t Francisco \n"

print(nome)

# Usando lstrip()
print(nome.rstrip())

# Usando rstrip()
print(nome.lstrip())

# Usando strip()
print(nome.strip())