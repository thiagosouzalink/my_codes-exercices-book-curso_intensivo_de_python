"""
9.5 – Tentativas de login: Acrescente um atributo chamado login_attempts à
sua classe User do Exercício 9.3 (página 226). Escreva um método chamado
increment_login_attempts() que incremente o valor de login_attempts em 1.
Escreva outro método chamado reset_login_attempts() que reinicie o valor de
login_attempts com 0.
Crie uma instância da classe User e chame increment_login_attempts()
várias vezes. Exiba o valor de login_attempts para garantir que ele foi
incrementado de forma apropriada e, em seguida, chame
reset_login_attempts(). Exiba login_attempts novamente para garantir que
seu valor foi reiniciado com 0.
"""

class User:

    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.login_attempts = 0

    def describe_user(self):
        print("\nInformações do Usuário:")
        print(f"Nome: {self.first_name}")
        print(f"Sobrenome: {self.last_name}")
        print(f"Idade: {self.age}")
        print(f"E-mail: {self.email}")

    def greet_user(self):
        print(f'Olá, {self.first_name}! Seja bem vindo(a)!')

    def increment_login_attempts(self):
        self.login_attempts += 1

    def reset_login_attempts(self):
        self.login_attempts = 0


user = User('José', 'Silva', 40, 'jose@mail.com')

user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
user.increment_login_attempts()
print(f'Tentativas de login: {user.login_attempts}')
user.reset_login_attempts()
print(f'Tentativas de login: {user.login_attempts}')