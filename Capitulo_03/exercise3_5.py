"""
convidados não poderá comparecer ao jantar, portanto será necessário enviar um novo conjunto de convites. Você deverá pensar em outra pessoa para convidar.
• Comece com seu programa do Exercício 3.4. Acrescente uma instrução print
no final de seu programa, especificando o nome do convidado que não poderá comparecer.
• Modifique sua lista, substituindo o nome do convidado que não poderá comparecer pelo nome da nova pessoa que você está convidando.
• Exiba um segundo conjunto de mensagens com o convite, uma para cada pessoa que continua presente em sua lista.
"""


convidados = ["Bill Gates", "Isaac Newton", "René Descartes"]

print(f"O convidado {convidados[2]} não poderá comparecer.\n")

convidados[2] = "Oswaldo Cruz"
print(f"Você está convidado paa nosso jantar, {convidados[0]}")
print(f"Você está convidado paa nosso jantar, {convidados[1]}")
print(f"Você está convidado paa nosso jantar, {convidados[2]}")