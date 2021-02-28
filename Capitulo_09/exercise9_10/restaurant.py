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