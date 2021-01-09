"""
6.3 – Glossário: Um dicionário Python pode ser usado para modelar um dicionário de verdade. No entanto, para evitar confusão, vamos chamá-lo de glossário.
• Pense em cinco palavras relacionadas à programação que você conheceu nos capítulos anteriores. Use essas palavras como chaves em seu glossário e armazene seus significados como valores.
• Mostre cada palavra e seu significado em uma saída formatada de modo elegante. Você pode exibir a palavra seguida de dois-pontos e depois o seu significado, ou apresentar a palavra em uma linha e então exibir seu significado indentado em uma segunda linha. Utilize o caractere de quebra de linha (\n) para inserir uma linha em branco entre cada par palavrasignificado em sua saída.
"""

glossario = {
    'string': 'conjunto de caracteres numa determinada ordem.',
    'variavel': 'são elementos que armazenam algum tipo de valor.',
    'codigo de maquina': 'Código que a máquina consegue entender e executar.',
    'bug': 'Problema no código que faz com que ele não execute sua função corretamente.',
    'algoritmo': 'Conjunto de passos para execução de uma tarefa.'
}

print(f"String: {glossario['string']}\n")
print(f"Variável: {glossario['variavel']}\n")
print(f"Código de Máquina: {glossario['codigo de maquina']}\n")
print(f"Bug: {glossario['bug']}\n")
print(f"Algoritmo: {glossario['algoritmo']}\n")
