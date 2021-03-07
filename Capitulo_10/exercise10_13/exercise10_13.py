"""
10.13 – Verificando se é o usuário correto: A última listagem de
remember_me.py supõe que o usuário já forneceu seu nome ou que o programa
está executando pela primeira vez. Devemos modificá-lo para o caso de o
usuário atual não ser a pessoa que usou o programa pela última vez.
Antes de exibir uma mensagem de boas-vindas de volta em greet_user(),
pergunte ao usuário se seu nome está correto. Se não estiver, chame
get_new_username() para obter o nome correto.
"""
import json


def get_stored_username():
    """Obtém o nome do usuário já armazenado se estiver disponível."""
    filename = 'username.json'

    try:
        with open(filename) as file_object:
            username = json.load(file_object)
    except FileNotFoundError:
        return None
    else:
        return username

def get_new_username():
    """Pede um novo nome de usuário"""
    username = input('Qual é o seu nome?: ').strip()
    filename = 'username.json'
    with open(filename, 'w') as file_object:
        json.dump(username, file_object)
    return username

def greet_user():
    """Saúda o usuário pelo nome."""
    username = get_stored_username()
    if username:
        print(f'Último visitante: {username}')
        confirm = input('Este usuário é você [s/n]: ').strip().lower()[0]
        while confirm not in 'sn':
            print('\nOpção inválida, tente novamente.')
            print(f'Último visitante: {username}')
            confirm = input('Este usuário é você [s/n]: ').strip().lower()[0]
        if confirm == 's':
            print(f'Bem vindo de volta, {username}!')
        else:
            username = get_new_username()
            print(f'Nós vamos lembrá-lo quando você voltar, {username}!')
    else:
        username = get_new_username()
        print(f'Nós vamos lembrá-lo quando você voltar, {username}!')


greet_user()

        