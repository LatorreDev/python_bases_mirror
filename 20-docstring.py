#!/usr/bin/env python3
"""Docstring en python 3"""
# Los docstrings son la manera de documentar nuestro codigo, es una practica que debe ser adquirida obligatoria

# Creamos una funcion que queremos documentar
def generador(*args):
    # Documentamos la funcion 
    """ Recibe n cantidad de numeros y regresa el numero ademas de regresar True o False
    si el numero es mayor a  5
    """
    for valor in args:
        yield valor, True if valor > 5 else False

# Imprimimos la documentacion
nombre = generador.__name__
documentacion = generador.__doc__
print(nombre, ":")
print(documentacion)

# Hay maneras de crear la documentacion usando api, frameworks, librearias o el interprete
