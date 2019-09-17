#!/usr/bin/env python3
"""Librerias en python 3"""
# Python es un lenguaje que se define "con baterias incluidas"
# Esto quiere decir que por defecto, trae muchas librerias

# Importamos una de las librerias que trae por default
import random # Nos permite generar enteros aleatorios
import datetime # Nos permite saber la hora actual del sistema
import sys # Nos permite trabajar con algunas opciones de nuestro sistema
import time # Nos permite gestionar delays en nuestro programa

valor = random.randint(0,10) # La variable valor retorna un entero aleatorio entre 0 y 10 mediante la libreria random y su metodo randint
# Imprimimos el valor
print(valor)

lista = [True, "strings", 23, False]
print("La lista es:", lista)
valor = random.choice( lista ) # Escoge aleatoriamente un valor en la lista
print(valor)
random.shuffle(lista) # mezcla aleatoriamente los valores en la lista
print(lista)

print(datetime.datetime.now()) #Nos imprime la hora actual

# Como hacer una barra de progreso con sys
for i in range (100):
    time.sleep(0.5)
    sys.stdout.write("\r%d %%" % i) # Imprime el numero de la iteracion en la misma posicion en la terminal
                                    # Un solo porcentage concatena, en este caso concatena con otro porcentaje
    sys.stdout.flush()
