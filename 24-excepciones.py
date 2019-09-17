#!/usr/bin/env python3
"""Excepciones en python 3"""

# Las excepciones son los manejos de errores que le podemos dar a nuestro programa para que no se rompa

# print(2/0)   Sabemos que no se puede dividir entre 0, por lo que el programa se rompe y no sigue ejecutando lo que continua
# Para evitar que se rompa y en caso de que falle siga ejecutando lo que sigue, usamos excepciones

try: # El try contiene todo el codigo que se intentara ejecutar
    print(2/0)
except ZeroDivisionError: # Except contiene el codigo que se ejecutara si el codigo del try falla, despues del except debemos poner que tipo de error manejaremos
    print("No es posible dividir entre 0")

# Otro ejemplo de try
try:
    lista = [1, 2] # La lista solo tiene dos elementos
    print(lista[9]) # Intentamos imprimir el valor en el indice 9 de la lista
except IndexError: # Manejo de error tipo IndexError
    print("el indice no existe, intente otro valor")

# Cuando no tenemos el tipo de error que vamos a manejar, podemos manejarlo asi

try:
    lista2= [1,2,3]
    print(lista[11])
except Exception: # Si no sabemos el tipo de error, usamos Exception
    print("Bien hecho, lo rompiste :(")

finally: # No importa si el codigo falla, lo que contenga finally, SIEMPRE se va a ejecutar
    print("Se termina la ejecucion del script")

