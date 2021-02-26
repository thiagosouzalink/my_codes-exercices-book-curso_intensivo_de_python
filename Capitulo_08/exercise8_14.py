"""
8.14 – Carros: Escreva uma função que armazene informações sobre um carro
em um dicionário. A função sempre deve receber o nome de um fabricante e um
modelo. Um número arbitrário de argumentos nomeados então deverá ser
aceito. Chame a função com as informações necessárias e dois outros pares
nome-valor, por exemplo, uma cor ou um opcional. Sua função deve ser
apropriada para uma chamada como esta: car = make_car(‘subaru’, ‘outback’,
color=’blue’, tow_package=True) Mostre o dicionário devolvido para garantir
que todas as informações foram armazenadas corretamente.
"""

def make_car(car_model, car_maker, **car_info):
    car = {}
    car['model'] = car_model
    car['maker'] = car_maker
    for key, value in car_info.items():
        car[key] = value
    return car


car1 = make_car('Ka', 'Ford', color='Cinza')
car2 = make_car('Gol', 'Volkswagen', ports=4, year=2020)

print(car1)
print(car2)