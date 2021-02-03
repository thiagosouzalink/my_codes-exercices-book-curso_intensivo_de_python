"""
7.10 – Férias dos sonhos: Escreva um programa que faça uma enquete sobre as
férias dos sonhos dos usuários. Escreva um prompt semelhante a este: Se
pudesse visitar um lugar do mundo, para onde você iria? Inclua um bloco de
código que apresente os resultados da enquete.
"""
enquete = {}
participantes = 0
while True:
    if not participantes:
        participar = input("Deseja participar da enquete [s/n]: ").strip()[0]
    else:
        participar = input("Deseja continuar participando da enquete [s/n]: ").strip()[0]
    
    if participar not in 'sn':
        print("Opção inválida, digite s ou n\n")
        continue
    if participar == "n":
        break
    
    nome = input("Digite seu nome: ").strip() 
    resposta = input("Se pudesse visitar um lugar do mundo, para onde você iria?: ").strip()
    enquete[nome] = resposta
    participantes += 1


if participantes:
    print("\nResultado da enquete:")
    for nome, resposta in enquete.items():
        print(f"  {nome.title()}: {resposta.title()}")
    print(f"\nTotal de partipiantes: {participantes}")
else:
    print("\nA enquete não teve participantes")