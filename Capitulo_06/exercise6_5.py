"""
6.5 – Rios: Crie um dicionário que contenha três rios importantes e o país que cada rio corta. Um par chave-valor poderia ser 'nilo': 'egito'.
• Use um laço para exibir uma frase sobre cada rio, por exemplo, O Nilo corre pelo Egito.
• Use um laço para exibir o nome de cada rio incluído no dicionário.
• Use um laço para exibir o nome de cada país incluído no dicionário.
"""

rios = {'amazonas': 'brasil', 'nilo': 'egito', 'mississipi': 'estados unidos'}

for rio, pais in rios.items():
    print(f"O rio {rio.capitalize()} corre pelo {pais.capitalize()}")

print("\nOs rios listados são: ")
for rio in rios.keys():
    print(rio.capitalize())

print("\nOs países listados são: ")
for pais in rios.values():
    print(pais.capitalize())