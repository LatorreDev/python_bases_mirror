#!/usr/bin/env python3
"""Generadores con python 3"""

# Nos sirven para poder crear objetos sin necesidad de almacenarlos en la memoria RAM
# Enumerate o range son generadores

# Creamos una funcion basica
def return_valores():
    print("Hola Mundo 1")
    return True

# Creamos nuestro generador
def generador(*args):
    # Por lo general se trabajan con un loop
    for valor in args:
        yield valor * 10 # yield toma la variable y la retorna para poder iterarla

# Llamamos nuestro generador
for valor in generador(1, 2, 3, 4, 5, 6, 7, 8, 9):
    print(valor)
