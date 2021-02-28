"""
9.2 – Três restaurantes: Comece com a classe do Exercício 9.1. Crie três
instâncias diferentes da classe e chame describe_restaurant() para cada
instância.
"""

class Restaurant:

    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print('\nInformações sobre o restaurante:')
        print(f"Nome do restaurante: {self.restaurant_name.title()}")
        print(f"Tipo de cozinha: {self.cuisine_type.title()}")

    def open_restaurant(self):
        print(f"\nO restaurante {self.restaurant_name} está aberto!")


restaurant1 = Restaurant('Point Paraense', 'Comida Paraense')
restaurant2 = Restaurant('Govinda Vegetariano', 'Comida vegetariana')
restaurant3 = Restaurant('Tutto', 'Comida Italiana')

restaurant1.describe_restaurant()
restaurant2.describe_restaurant()
restaurant3.describe_restaurant()