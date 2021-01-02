"""
5.11 – Números ordinais: Números ordinais indicam sua posição em uma lista, por exemplo, 1st ou 2nd, em inglês. A maioria dos números ordinais nessa língua termina com th, exceto 1, 2 e 3.
• Armazene os números de 1 a 9 em uma lista.
• Percorra a lista com um laço.
• Use uma cadeia if-elif-else no laço para exibir a terminação apropriada para cada número ordinal. Sua saída deverá conter "1st 2nd 3rd 4th 5th 6th 7th 8th 9th", e cada resultado deve estar em uma linha separada.
"""

numbers = list(range(1, 10))

for number in numbers:
    termination = 'th'
    if number == 1 or number == 2 or number == 3:
        if number == 1:
            termination = 'st'
        elif number == 2:
            termination = 'nd'
        else:
            termination = 'rd'
    print(f"{number}{termination}")