#!/usr/bin/env python3
"""Funciones anidadas en python 3"""
# Si tengo una funcion que realiza una tarea que solo se ejecuta si es llamada por otra funcion
# Podemos usar funciones anidadas

#Funciones separadas normalmente
def validacion(num_uno, num_dos):
    return num_uno > 0 and num_dos > 0

def division(num_uno, num_dos):
    if validacion(num_uno, num_dos):
        return num_uno / num_dos

resultado = division(10,0)
print("La division es:",resultado)

# funciones anidadas
def multiplicacion(num_uno, num_dos):
    def validacion(): # Esto es una funcion anidada
        return num_uno > 0 and num_dos > 0

    if validacion(): #No son necesarios argumentos ni parametros 
                     # ya que al ser anidada toma los parametros y variables
                     # pasados a la funcion padre como variables locales
        return num_uno / num_dos
resultado =  multiplicacion(6, 7)
print("La multiplicacion es:",resultado)

# Closures, funciones que crean funciones
def crear_funcion(num_uno, num_dos):
    print("Se ejecuta validacion")
    def validacion(): # Funcion anidada
        return num_uno > 0 and num_dos > 0

    return validacion

nueva_funcion = crear_funcion(10, 8)
# algoritmo
print(nueva_funcion()) # No necesita tomar argumentos ya que nueva funcion tiene los argumentos

# Como crear una funcion que reciba otra funcion

def aplicar_funcion(func):
    resultado = func() # Retorna True or False
    print(resultado)
aplicar_funcion(nueva_funcion)

# Crear funcion regresa validacion
# Ese return se aplica como parametro a aplicar_funcion
# Aplicar funcion ejecuta func
# Lo que deberia ejecutar validacion

# Una funcion puede tener como argumento otra funcion
