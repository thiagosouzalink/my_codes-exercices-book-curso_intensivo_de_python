"""
10.2 – Aprendendo C: Você pode usar o método replace() para substituir
qualquer palavra por uma palavra diferente em uma string. Eis um exemplo
rápido que mostra como substituir a palavra 'dog' por 'cat' em uma frase:
message = "I really like dogs."
message.replace('dog', 'cat') 'I really like cats.'
Leia cada linha do arquivo learning_python.txt que você acabou de criar e
substitua a palavra Python pelo nome de
"""

filename = 'learning_python.txt'

with open(filename, encoding='UTF-8') as file_object:
    lines = file_object.readlines()
for line in lines:
    print(line.strip().replace('Python', 'C'))