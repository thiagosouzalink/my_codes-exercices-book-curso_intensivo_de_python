"""
9.13 – Reescrevendo o programa com OrderedDict: Comece com o Exercício
6.4 (página 155), em que usamos um dicionário-padrão para representar um
glossário. Reescreva o programa usando a classe OrderedDict e certifique-se de
que a ordem da saída coincida com
"""

from collections import OrderedDict


glossario = OrderedDict()

glossario['string'] = 'conjunto de caracteres numa determinada ordem.'
glossario['variavel'] = 'são elementos que armazenam algum tipo de valor.'
glossario['codigo de maquina'] = 'Código que a máquina consegue entender e executar.'
glossario['bug'] = 'Problema no código que faz com que ele não execute sua função corretamente.'
glossario['algoritmo'] = 'Conjunto de passos para execução de uma tarefa.'

for palavra, significado in glossario.items():
    print(f"{palavra.capitalize()}: {significado.capitalize()}\n")  