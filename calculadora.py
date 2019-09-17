#!/usr/bin/env python3

"""Funciones de calculadora en python 3"""

__author__ = "David Latorre"
__copyright__ = "David Latorre 2019"
__credits__ = "Codigo facilito"

__license__ = "GPL"
__version__ = "1.0.1"
__maintainer__ = "David Latorre"
__email__ = "david@latorredev.com"
__status__ = "Python Backend and DevOps"

def suma(num_uno, num_dos):
    """ Regresa un numero entero el cual es el resultado de una suma"""
    return num_uno + num_dos

def resta(num_uno, num_dos):
    """ Regresa un numero entero el cual es el resultado de una resta"""
    return num_uno - num_dos

def multiplicacion(num_uno, num_dos):
    """ Regresa un numero entero el cual es el resultado de una multiplicacion"""
    return num_uno * num_dos

def division(num_uno, num_dos):
    """ Regresa un numero entero el cual es el resultado de una division"""
    return num_uno / num_dos

# Si este archivo se va a usar como modulo, se deben quitar todos los llamados a funciones
# Se debe incluir el shebang (#!/usr/bin/env python3)
# Documentar el modulo con comillas triples (""")
# Incluir metadatas, ejemplo __license__, __copyright__, etc.
