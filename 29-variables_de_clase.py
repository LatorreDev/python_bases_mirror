#!/usr/bin/env python3
""" Variables de clase en python 3"""

# Las variables de clase perteneces a la clase y no a los metodos

class Circulo:

    _pi = 3.1416    # No existen las constantes en Python, por lo que por convencion se usa un guion bajo antes del nombre de una variable
                    # para indicarle a un desarrollador que no hay que modificar su valor

    def __init__(self, radio):
        self.radio = radio

    def area(self):
        return self.radio * self.radio * Circulo.pi

circulo_uno = Circulo(4)
circulo_dos = Circulo(3)

print(Circulo.pi) # No necesitamos crear un objeto para usar PI

print(circulo_uno.pi)
print(circulo_dos.pi)

print(circulo_uno.__dict__) # Nos muestra todos los atributos de la clase

print(circulo_uno.area())

