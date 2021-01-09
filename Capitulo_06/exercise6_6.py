"""
6.6 – Enquete: Utilize o código em favorite_languages.py (página 150).
• Crie uma lista de pessoas que devam participar da enquete sobre linguagem favorita. Inclua alguns nomes que já estejam no dicionário e outros que não estão.
• Percorra a lista de pessoas que devem participar da enquete. Se elas já tiverem respondido à enquete, mostre uma mensagem agradecendo-lhes por responder. Se ainda não participaram da enquete, apresente uma mensagem convidando-as a responder.
"""
participantes = ['thiago', 'sarah', 'jen', 'paulo', 'edward', 'jessica']
favorite_languages = {'jen': 'python', 'sarah': 'c', 'edward': 'ruby', 'phil': 'python',}

for nome in participantes:
    if nome in favorite_languages.keys():
        print(f"Obrigado por já ter respondido à nossa enquete, {nome.capitalize()}!")
    else:
        print(f"Você está convidado a responder à nossa enquete, {nome.capitalize()}.") 