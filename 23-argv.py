#!/usr/bin/env python3
"""Argumentos en python 3"""

# argv nos permite pasar diferentes parametros al llamar el programa y reutilizarlos en funciones internas del mismo

# Ejemplo
# /.miprograma.py this is python
# En este caso el programa tiene 3 argumentos
# this es el primero, is es el segundo y python es el tercero

import sys

if __name__ == '__main__':
    if len(sys.argv) == 1: # Verifica si los argumentos pasados es igual a 1
        print("Es necesario colocar por lo menos un argumento")
    else:
        if sys.argv[1] == 'help': # Verifica si el argumento pasado es igual a help ejecute el codigo que sigue
            print("Puedes contactar a David Latorre si tienes alguna duda")
