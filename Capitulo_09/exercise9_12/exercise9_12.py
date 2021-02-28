"""
9.12 – Vários módulos: Armazene a classe User em um módulo e as classes
Privileges e Admin em um módulo separado. Em outro arquivo, crie uma
instância de Admin e chame show_privileges() para mostrar que tudo continua
funcionando de forma apropriada.
"""

from admin import Admin, Privileges


admin1 = Admin('Maria', 'Silva', 25, 'maria@mail.com')
admin1.privilege.show_privileges()