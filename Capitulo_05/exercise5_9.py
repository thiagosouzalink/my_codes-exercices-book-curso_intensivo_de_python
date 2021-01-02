"""
5.9 – Sem usuários: Acrescente um teste if em hello_admin.py para garantir que a lista de usuários não esteja vazia.
• Se a lista estiver vazia, mostre a mensagem Precisamos encontrar alguns usuários!
• Remova todos os nomes de usuário de sua lista e certifique-se de que a mensagem correta seja exibida.
"""

users = ['erik', 'jose', 'admin', 'maria', 'joana']

if users:
    for user in users:
        if user == 'admin':
            print("Olá admin, gostaria de ver um relarório de status?")
        else:
            print(f"Olá {user.capitalize()}, obrigado por fazer login novamente.")
else:
    print("Precisamos encontrar alguns usuários!")




print()
users = []
if users:
    for user in users:
        if user == 'admin':
            print("Olá admin, gostaria de ver um relarório de status?")
        else:
            print(f"Olá {user.capitalize()}, obrigado por fazer login novamente.")
else:
    print("Precisamos encontrar alguns usuários!")
