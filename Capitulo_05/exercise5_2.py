"""
5.2 – Mais testes condicionais: Você não precisa limitar o número de testes que criar em dez. Se quiser testar mais comparações, escreva outros testes e acrescente-os em conditional_tests.py. Tenha pelo menos um resultado True e um False para cada um dos casos a seguir: 
• testes de igualdade e de não igualdade com strings; 
• testes usando a função lower(); 
• testes numéricos que envolvam igualdade e não igualdade, maior e menor que, maior ou igual a e menor ou igual a; 
• testes usando as palavras reservadas and e or; 
• testes para verificar se um item está em uma lista; 
• testes para verificar se um item não está em uma lista.
"""

# String
fruta = 'Maçã'
numero = 5
lista = ['São Paulo', 'Belém', 'Recife', 'Curitiba']

print(fruta=='Pêra')
print(fruta=='Maçã')

print()
print(fruta=='Maçã')
print(fruta=='Maçã'.lower())

print()
print(numero==10)
print(numero==5)
print(numero < 6)
print(numero > 8)

print()
print(numero > 2 and numero < 4)
print(numero > 0 and numero < 10)
print(numero < 1 or numero > 3)
print(numero < 3 or numero > 6)

print()
print('Rio de Janeiro' in lista)
print('São Paulo' in lista)