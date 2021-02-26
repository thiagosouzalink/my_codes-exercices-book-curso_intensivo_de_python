"""
8.16 – Importações: Usando um programa que você tenha escrito e que
contenha uma única função, armazene essa função em um arquivo separado.
Importe a função para o arquivo principal de seu programa e chame-a usando
cada uma das seguintes abordagens: import nome_do_módulo from
nome_do_módulo import nome_da_função from nome_do_módulo import
nome_da_função as nf import nome_do_módulo as nm from nome_do_módulo import
*
"""
# import car_function
# from car_function import make_car
# from car_function import make_car as mc
# import car_function as cf
from car_function import *


# car1 = car_function.make_car('Ka', 'Ford', color='Cinza')
# car2 = car_function.make_car('Gol', 'Volkswagen', ports=4, year=2020)

# car1 = make_car('Ka', 'Ford', color='Cinza')
# car2 = make_car('Gol', 'Volkswagen', ports=4, year=2020)

# car1 = mc('Ka', 'Ford', color='Cinza')
# car2 = mc('Gol', 'Volkswagen', ports=4, year=2020)

# car1 = cf.make_car('Ka', 'Ford', color='Cinza')
# car2 = cf.make_car('Gol', 'Volkswagen', ports=4, year=2020)

car1 = make_car('Ka', 'Ford', color='Cinza')
car2 = make_car('Gol', 'Volkswagen', ports=4, year=2020)

print(car1)
print(car2)