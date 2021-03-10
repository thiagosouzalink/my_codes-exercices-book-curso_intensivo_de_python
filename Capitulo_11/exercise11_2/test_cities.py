"""
11.2 – População: Modifique sua função para que ela exija um terceiro
parâmetro, population. Agora ela deve devolver uma única string no formato Cidade, País – população xxx, por exemplo, Santiago, Chile – população
5000000. Execute test_cities.py novamente. Certifique-se de que
test_city_country() falhe dessa vez.
Modifique a função para que o parâmetro population seja opcional. Execute
test_cities.py novamente e garanta que test_city_country() passe novamente.
Escreva um segundo teste chamado test_city_country_population() que
verifique se você pode chamar sua função com os valores 'santiago', 'chile' e
'population=5000000'. Execute test_cities.py novamente e garanta que esse
novo teste passe.
"""

import unittest
from city_functions import city_country


class CityCountryTestCase(unittest.TestCase):

    def test_city_country(self):
        city_country_formatted = city_country('santiago', 'chile')
        self.assertEqual(city_country_formatted, 'Santiago, Chile')

    def test_city_country_population(self):
        city_country_formatted = city_country('santiago', 'chile', population=5000000)
        self.assertEqual(city_country_formatted, 'Santiago, Chile - população 5000000')

unittest.main()