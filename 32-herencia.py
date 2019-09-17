#!/usr/bin/env python3
""" Herencia en python 3"""

# Es un mecanismo de la programacion orientada a objetos la cual nos permitira crear una clase a partir de clases ya existentes
# Usaremos en este ejemplo dos clases y dos isntancias

# Aprendamos a aplicar el principio DRY(don't repeat yourself)

class Animal:
    @property
    def terrestre(self):
        return(True)

class Felino(Animal): # Clase Padre
    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("el felino esta cazando")


class Gato(Felino): # Para heredar usamos parentesis y la clase padre
    def gato_cazador(self):
        self.cazar()

class Jaguar(Felino):
    pass

gato = Gato()
jaguar = Jaguar()

print(gato.gato_cazador())
print(jaguar.garras_retractiles)
print(gato.terrestre)
print(jaguar.terrestre)
