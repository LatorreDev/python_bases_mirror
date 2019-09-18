#!/usr/bin/env python3
""" Override en python 3"""

# La herencia multiple nos permite heredar de distintas clases

class Mascota:
    nombre = '' # Todas las mascotas llevan un nombre

    def mostrar_nombre(self):
        print(self.nombre)

    def __init__(self, nombre):
        self.nombre = nombre

class Animal:
    pass

class Felino(Animal):
    pass

class Gato(Felino, Mascota): # Es tan sencillo como invocar una segunda clase, precedida de una coma
    def __init__(self, nombre):
        Mascota.__init__(self, nombre)
        self.nombre_gato = nombre

    def gato_cazador(self):
        self.cazar()

    def mostrar_nombre(self): # Sobre escritura de metodos
        Mascota.mostrar_nombre(self) # Asi llamamos el metodo desde la clase padre
        print("El nombre del gato es: {}".format(self.nombre))

# Al ejecutarse busca primero los metodos que estan declarados dentro de la clase, si no, usa los metodos de las clases que esta heredando
# Siempre busca de izquierda a derecha en las clases heredadas

gato = Gato("Patricio")
# gato.nombre = 'Patricio'
gato.mostrar_nombre()
