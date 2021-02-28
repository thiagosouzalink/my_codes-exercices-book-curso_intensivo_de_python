"""
9.7 – Admin: Um administrador é um tipo especial de usuário. Escreva uma
classe chamada Admin que herde da classe User escrita no Exercício 9.3
(página 226), ou no Exercício 9.5 (página 232). Adicione um atributo
privileges que armazene uma lista de strings como "can add post", "can
delete post" "can ban user", e assim por diante. Escreva um método chamado
show_privileges() que liste o conjunto de privilégios de um administrador. Crie
uma instância de Admin e chame seu método.
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
        self.privileges = ['Pode add post', 'Pode excluir post', 'Pode banir usuário']
    
    def show_privileges(self):
        print(f'Privilégios do administrador {self.first_name}: ')
        for privilege in self.privileges:
            print (privilege)

admin = Admin('José', 'Silva', 40, 'jose@mail.com')
admin.show_privileges()

