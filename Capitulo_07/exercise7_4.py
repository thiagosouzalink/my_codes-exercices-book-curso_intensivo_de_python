"""
7.4 – Ingredientes para uma pizza: Escreva um laço que peça ao usuário para
fornecer uma série de ingredientes para uma pizza até que o valor 'quit' seja
fornecido. À medida que cada ingrediente é especificado, apresente uma
mensagem informando que você acrescentará esse ingrediente à pizza.
"""

while True:
    ingrediente = input("Digite um ingrediente, 'quit' para sair: ").strip()
    if ingrediente == "quit":
        print("Obrigado!")
        break
    print(f"Ingrediente {ingrediente} acrescentado à pizza.\n")