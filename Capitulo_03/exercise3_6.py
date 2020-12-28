"""
3.6 – Mais convidados: Você acabou de encontrar uma mesa de jantar maior, portanto agora tem mais espaço disponível. Pense em mais três convidados para o jantar.
• Comece com seu programa do Exercício 3.4 ou do Exercício 3.5. Acrescente uma instrução print no final de seu programa informando às pessoas que você encontrou uma mesa de jantar maior.
• Utilize insert() para adicionar um novo convidado no início de sua lista.
• Utilize insert() para adicionar um novo convidado no meio de sua lista.
• Utilize append() para adicionar um novo convidado no final de sua lista.
• Exiba um novo conjunto de mensagens de convite, uma para cada pessoa que está em sua lista.
"""


convidados = ["Bill Gates", "Isaac Newton", "René Descartes"]

print(f"O convidado {convidados[2]} não poderá comparecer.")

convidados[2] = "Oswaldo Cruz"

print("\nEncontrei uma mesa de jantar maior! Vamos convidar mais pessoas!\n")

convidados.insert(0, "Ronaldo")
convidados.insert(2, "Carl Gauss")
convidados.append("Albert Einstein")

print(f"Você está convidado paa nosso jantar, {convidados[0]}")
print(f"Você está convidado paa nosso jantar, {convidados[1]}")
print(f"Você está convidado paa nosso jantar, {convidados[2]}")
print(f"Você está convidado paa nosso jantar, {convidados[3]}")
print(f"Você está convidado paa nosso jantar, {convidados[4]}")
print(f"Você está convidado paa nosso jantar, {convidados[5]}")