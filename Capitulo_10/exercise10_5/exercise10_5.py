"""
10.5 – Enquete sobre programação: Escreva um laço while que pergunte às
pessoas por que elas gostam de programação. Sempre que alguém fornecer um
motivo, acrescente-o em um arquivo que armazene todas as respostas.
"""

while True:
    poll = input('\nPor que você gosta de programação: ').strip()

    if poll:
        with open('poll_responses.txt', 'a', encoding='UTF-8') as file_object:
            file_object.write(f'{poll}\n')

    cont = input('\nDeseja continuar? [s/n]: ').strip().lower()[0]
    while cont not in 'sn':
        print('Opção inválida, tente novamente.')
        cont = input('\nDeseja continuar? [s/n]: ').strip().lower()[0]
    
    if cont == 'n':
        break
