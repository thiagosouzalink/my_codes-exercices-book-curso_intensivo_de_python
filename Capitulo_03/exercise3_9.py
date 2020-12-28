"""
3.9 – Convidados para o jantar: Trabalhando com um dos programas dos Exercícios de 3.4 a 3.7 (páginas 80 e 81), use len() para exibir uma mensagem informando o número de pessoas que você está convidando para o jantar.
"""

# Exercício 3.6
convidados = ["Bill Gates", "Isaac Newton", "René Descartes"]

print(f"O convidado {convidados[2]} não poderá comparecer.")

convidados[2] = "Oswaldo Cruz"

print("\nEncontrei uma mesa de jantar maior! Vamos convidar mais pessoas!\n")

convidados.insert(0, "Ronaldo")
convidados.insert(2, "Carl Gauss")
convidados.append("Albert Einstein")

print(f"Número de pessoas convidados para o jantar: {len(convidados)}")