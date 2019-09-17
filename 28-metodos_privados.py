#!/usr/bin/env python3
"""Metodos privados en python 3"""

# Los atributos privados solo pueden ser modificados por la clase y no su instancia
# Un atributo privado lleva doble guion bajo al inicio

class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.gen_pass(password) # Atributo privado
        self.email = email

    def __gen_pass(self, password):
        return password.upper()

david = Usuario("David90", "my_password", "david@latorredev.com")
print(david.username)
# print(david.password) No se puede acceder, ya que solo puede ser accedido por la clase
print(david.email)
