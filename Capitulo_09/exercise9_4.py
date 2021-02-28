"""
9.4 – Pessoas atendidas: Comece com seu programa do Exercício 9.1 (página
225). Acrescente um atributo chamado number_served cujo valor default é 0.
Crie uma instância chamada restaurant a partir dessa classe. Apresente o
número de clientes atendidos pelo restaurante e, em seguida, mude esse valor e
exiba-o novamente.
Adicione um método chamado set_number_served() que permita definir o
número de clientes atendidos. Chame esse método com um novo número e
mostre o valor novamente.
Acrescente um método chamado increment_number_served() que permita
incrementar o número de clientes servidos. Chame esse método com qualquer
número que você quiser e que represente quantos clientes foram atendidos, por
exemplo, em um dia de funcionamento.
"""

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_restaurant(self):
        print('\nInformações sobre o restaurante:')
        print(f"Nome do restaurante: {self.restaurant_name.title()}")
        print(f"Tipo de cozinha: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"\nO restaurante {self.restaurant_name} está aberto!")

    def set_number_served(self, number_served):
        self.number_served = number_served

    def increment_number_served(self):
        self.number_served += 1


restaurant = Restaurant('Tutto', 'Comida Italiana')

print(f'Clientes atendidos: {restaurant.number_served}')
restaurant.number_served = 5
print(f'Clientes atendidos: {restaurant.number_served}')

restaurant.set_number_served(9)
print(f'Clientes atendidos: {restaurant.number_served}')

restaurant.increment_number_served()
restaurant.increment_number_served()
restaurant.increment_number_served()
print(f'Clientes atendidos: {restaurant.number_served}')

