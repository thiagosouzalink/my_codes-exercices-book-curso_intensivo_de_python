"""
9.1 – Restaurante: Crie uma classe chamada Restaurant. O método __init__()
de Restaurant deve armazenar dois atributos: restaurant_name e
cuisine_type. Crie um método chamado describe_restaurant() que mostre
essas duas informações, e um método de nome open_restaurant() que exiba
uma mensagem informando que o restaurante está aberto.
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


restaurant = Restaurant('Point Paraense', 'Comida Paraense')
print(restaurant.restaurant_name)
print(restaurant.cuisine_type)

restaurant.describe_restaurant()
restaurant.open_restaurant()    