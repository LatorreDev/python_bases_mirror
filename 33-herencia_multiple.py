#!/usr/bin/env python3
""" Herencia multiple en python 3"""

# La herencia multiple nos permite heredar de distintas clases

class Mascota:
    nombre = '' # Todas las mascotas llevan un nombre

    def mostrar_nomre(self):
        print(self.nombre)

class Animal:
    @property
    def terrestre(self):
        return True

class Felino(Animal):
    @property
    def garras_retractiles(self):
        return True

    def cazar(self):
        print("El felino esta cazando")

class Gato(Felino, Mascota): # Es tan sencillo como invocar una segunda clase, precedida de una coma
    def gato_cazador(self):
        self.cazar()

gato = Gato()
gato.nombre = 'Gato con nombre'
print(gato.terrestre)
