"""
4.12 – Mais laços: Todas as versões de foods.py nesta seção evitaram usar laços for para fazer exibições a fim de economizar espaço. Escolha uma versão de foods.py e escreva dois laços for para exibir cada lista de comidas
"""

my_foods = ['pizza', 'falafel', 'carrot cake']

friend_foods = my_foods[:]

my_foods.append('cannoli')
friend_foods.append('ice cream')

print("minhas comidas favoritas são:")
for food in my_foods:
    print(f"   {food}")

print("\nAs comidas favoritas de meu amigo são:")
for food in friend_foods:
    print(f"   {food}")