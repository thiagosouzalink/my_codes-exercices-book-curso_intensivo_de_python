"""
9.8 – Privilégios: Escreva uma classe Privileges separada. A classe deve ter um
atributo privileges que armazene uma lista de strings conforme descrita no
Exercício 9.7. Transfira o método show_privileges() para essa classe. Crie
uma instância de Privileges como um atributo da classe Admin. Crie uma nova
instância de Admin e use seu método para exibir os privilégios.
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


class Admin(User):

    def __init__(self, first_name, last_name, age, email):
        super().__init__(first_name, last_name, age, email)
        self.privilege = Privileges()
    

class Privileges:

    def __init__(self):
        self.privileges = ['Pode add post', 'Pode excluir post', 'Pode banir usuário']

    def show_privileges(self):
        print(f'Privilégios do administrador: ')
        for privilege in self.privileges:
            print (privilege)


admin = Admin('Paulo', 'Oliveira', 35, 'paulo@mail.com')
admin.privilege.show_privileges()