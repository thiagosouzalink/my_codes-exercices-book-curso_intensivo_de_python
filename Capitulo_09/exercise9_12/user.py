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


