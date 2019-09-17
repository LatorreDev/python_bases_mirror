#!/usr/bin/env python3
"""Propierties en python 3"""


# Con los propierties podemos trabajar con los metodos privados de una clase

class Usuario:
    def __init__(self, username, password, email):
        self.username = username
        self.__password = self.__generar_password(password)
        self.email = email

    def __generar_password(self, password):
        return password.upper()

    @property
    def password(self):
        return self.__password # Solo existe para visualizar, no para modificar

    @password.setter
    def password(self, valor): # Va a generar un nuevo string a partir del que le pasemos y se lo va a asignar al atributo privado
        self.__password = self.__generar_password(valor)


david = Usuario('David', 'David123', 'david@latorredev.com')
print (david.password)
david.password = 'Nuevo password'
print(david.password)
