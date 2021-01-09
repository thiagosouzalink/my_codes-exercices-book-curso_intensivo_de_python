"""
6.4 – Glossário 2: Agora que você já sabe como percorrer um dicionário com um laço, limpe o código do Exercício 6.3 (página 148), substituindo sua sequência de instruções print por um laço que percorra as chaves e os valores do dicionário. Quando tiver certeza de que seu laço funciona, acrescente mais cinco termos de Python ao seu glossário. Ao executar seu programa novamente, essas palavras e significados novos deverão ser automaticamente incluídos na saída.
"""

glossario = {
    'string': 'conjunto de caracteres numa determinada ordem.',
    'variavel': 'são elementos que armazenam algum tipo de valor.',
    'codigo de maquina': 'Código que a máquina consegue entender e executar.',
    'bug': 'Problema no código que faz com que ele não execute sua função corretamente.',
    'algoritmo': 'Conjunto de passos para execução de uma tarefa.'
}

for palavra, significado in glossario.items():
    print(f"{palavra.capitalize()}: {significado.capitalize()}\n")  

# Adicionar mais 5 palavras com seu significado e executar novamente o laço.