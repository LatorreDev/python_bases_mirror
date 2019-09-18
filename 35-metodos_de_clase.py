#!/usr/bin/env python3
""" Metodos de clase """

# Los metodos de clase le perteneces a la clase, es decir los podemos usar sin necesidad de crear un objeto
# Los metodos de clase pueden acceder a los atributos de las clases que esta heredando, los metodos estaticos no.

class Animal:
    volador = True

class Cocodrilo(Animal):

    def __init__(self, nombre):
        self.nombre = nombre

    @classmethod # Este decorador junto a cls reemplazando a self, convierte a nuestro metodo en parte de la clase y no de la instancia
    def new(cls, nombre):
        return Cocodrilo(nombre)

cocodrilo = Cocodrilo.new('coco')
print(cocodrilo.nombre)
print(cocodrilo.volador)
