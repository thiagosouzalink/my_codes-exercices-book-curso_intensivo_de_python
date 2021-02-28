"""
9.11 – Importando Admin: Comece com seu programa do Exercício 9.8 (página
241). Armazene as classes User, Privileges e Admin em um módulo. Crie um
arquivo separado e uma instância de Admin e chame show_privileges() para
mostrar que tudo está funcionando de forma apropriada.
9.12 – Vários módulos: Armazene a classe User em um
"""

from user import User, Privileges, Admin


admin = Admin('João', 'Pereira', 40, 'joao@mail.com')
admin.privilege.show_privileges()