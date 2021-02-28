"""
9.6 – Sorveteria: Uma sorveteria é um tipo específico de restaurante. Escreva
uma classe chamada IceCreamStand que herde da classe Restaurant escrita no
Exercício 9.1 (página 225) ou no Exercício 9.4 (página 232). Qualquer
versão da classe funcionará; basta escolher aquela de que você mais gosta.
Adicione um atributo chamado flavors que armazene uma lista de sabores de
sorvete. Escreva um método para mostrar esses sabores. Crie uma instância de
IceCreamStand e chame esse método.
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


class IceCreamStand(Restaurant):

    def __init__(self, restaurant_name, cuisine_type, flavors):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = flavors

    def show_flavors(self):
        print("Sabores disponíveis: ")
        for flavor in self.flavors:
            print(flavor)
        


flavors = ['Chocolate', 'Tapioca', 'Morango', 'Coco Nevado', 'Baunilha', 'Açaí']
icecreamshop = IceCreamStand('Icebode', 'Sorveteria', flavors)
icecreamshop.show_flavors()