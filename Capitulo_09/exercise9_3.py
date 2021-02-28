"""
9.3 – Usuários: Crie uma classe chamada User. Crie dois atributos de nomes
first_name e last_name e, então, crie vários outros atributos normalmente
armazenados em um perfil de usuário. Escreva um método de nome
describe_user() que apresente um resumo das informações do usuário. Escreva
outro método chamado greet_user() que mostre uma saudação personalizada
ao usuário.
Crie várias instâncias que representem diferentes usuários e chame os dois
métodos para cada usuário.
"""

class User:

    def __init__(self, first_name, last_name, age, email):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email

    def describe_user(self):
        print("\nInformações do Usuário:")
        print(f"Nome: {self.first_name}")
        print(f"Sobrenome: {self.last_name}")
        print(f"Idade: {self.age}")
        print(f"E-mail: {self.email}")

    def greet_user(self):
        print(f'Olá, {self.first_name}! Seja bem vindo(a)!')


user1 = User('Thiago', 'Souza', 31, 'thiago@mail.com')
user2 = User('Paulo', 'Silva', 36, 'paulo@mail.com')
user3 = User('Maria', 'Silveira', 20, 'maria@mail.com')
user4 = User('Jessica', 'Herminio', 28, 'jessica@mail.com')
user5 = User('Kaleb', 'Guimarães', 16, 'kaleb@mail.com')

user1.greet_user()
user2.greet_user()
user3.greet_user()
user4.greet_user()
user5.greet_user()

user1.describe_user()
user2.describe_user()
user3.describe_user()
user4.describe_user()
user5.describe_user()

