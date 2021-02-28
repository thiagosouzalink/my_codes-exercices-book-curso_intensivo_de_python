from user import User


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