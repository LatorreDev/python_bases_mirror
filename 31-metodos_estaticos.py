#!/usr/bin/env python3
""" Metodos estaticos en python 3 """

# Los metodos no son mas que funciones que se encuentran dentro de una clase
# cuando un metodo tiene la palabra reservada self, son metodos de instancia
# Lo que quiere decir que un objeto puede llamarlos

# Si no tiene la palabra self, es un metodo estatico, tambien pertenecen a la clase y no a la instancia

# En python existen varios metodos, en este caso veremos el metodo estatico

class Circulo:

    @staticmethod # Usamos este decorador, es obligatorio para crear un metodo estatico
    def pi():
        return 3.1416

    def __init__(self, radio):
        self.radio =  radio

    def area(self): # Metodo de instancia
        return self.radio * self.radio * self.pi() # Nos fijamos en como es llamado pi, como un metodo de si mismo

circulo_uno = Circulo(7)
print(circulo_uno.area())
