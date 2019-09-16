#!/usr/bin/env python3
"""Archivo Main"""
# importamos el archivo que queremos
import calculadora #No es necesario llamarlo con su extension

# Otras formas de usar las funcionalidades de un modulo
from calculadora import suma, resta # se importan dos funciones de calculadora
from calculadora import multiplicacion as mult  # Al llamar multiplicacion se llamara como mult al importar
                                                # de este modo ya que al usar "as" podemos renombrar

# Otra forma de importr es 
# from calculadora import * 
# No es comun hacerlo asi, ya que importa todo, consume mas recursos y un desarrollador nuevo del equipo
# desconocera que funcionalidades tiene el modulo importado

resultado = calculadora.suma(30, 45)    # debemos llamar las funciones internas del programa importado
                                        # como un metodo y pasarle los valores requeridos en caso de que
                                        # los necesite
print(resultado)

resultado2 = calculadora.resta(5, 3)
print(resultado2)

# Al correr modulos se crea una carpeta llamada __pycache__
# La cual contiene un programa con el mismo nombre del programa que corrimos solo que la
# extension es .pyc, lo cual significa que es un archivo compilado de python
# Es creado para reducir el tiempo de ejecucion al volver a correr el programa ya que tomara
# directamente el archivo compilado
