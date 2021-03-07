"""
10.4 – Lista de convidados: Escreva um laço while que pergunte o nome aos
usuários. Quando fornecerem seus nomes, apresente uma saudação na tela e
acrescente uma linha que registre a visita do usuário em um arquivo chamado
guest_book.txt. Certifique-se de que cada entrada esteja em uma nova linha do
arquivo.
"""

while True:
    guest = input('\nDigite o nome do usuário: ').strip()
    salute_guest = f'Bem vindo(a), {guest}!'
    print(salute_guest)
    
    with open('guest_book.txt', 'a', encoding='UTF-8') as file_object:
        file_object.write(f'{salute_guest}\n')
    
    cont = input('\nDeseja continuar [s/n]?: ').strip().lower()[0]
    while cont not in 'sn':
        print('\nOpção inválida, tente novamente.')
        stop = input('Deseja continuar [s/n]?: ').strip().lower()[0]
    
    if cont == 'n':
        break
