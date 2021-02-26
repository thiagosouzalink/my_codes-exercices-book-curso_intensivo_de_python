"""
8.6 – Nomes de cidade: Escreva uma função chamada city_country() que
aceite o nome de uma cidade e seu país. A função deve devolver uma string
formatada assim: "Santiago, Chile"
Chame sua função com pelo menos três pares cidade-país e apresente o valor
devolvido.
"""

def city_country(city, country):
    return f"{city}, {country}"


cidade1 = city_country("Belém", "Brasil")
cidade2 = city_country("Nova York", "Estados Unidos")
cidade3 = city_country("Amsterdã", "Holanda")

print(cidade1)
print(cidade2)
print(cidade3)
