#!/usr/bin/env python3
"""Argumentos en Python"""

# Cuando necesitamos pasar n cantidad de argumentos a una funcion lo hacemos de la siguiente manera
def ejemplo(*argumento): # el * indica que va a recibir n cantidad de argumentos
    print(argumento)

# ejemplo operativo
def suma(*args): #Por convencion general se usa la palabra args, pero esta puede cambiarse a gusto, no influye
    resultado = 0 # inicializamos una variable en 0
    for valor in args:
        resultado = resultado + valor
    return resultado

resultado = suma(1, 2, 3, 4, 5, 6, 7, 8, 9)
print(resultado)

# Si necesitamos n cantidad de argumentos pero con el nombre de variables especificas
# anteriormente lo haciamos asi
# def suma(valor_uno = 100, valor_dos = 200)
# Ahora lo hacemos asi, usando kwargs
def ejemplo2(**kwargs):
    valor = kwargs.get('valor', 'no contiene el valor')
    print(valor)

resultado = ejemplo2(valor = 'David', x = 2, y = 9, z = True)
print(resultado)
# con un asterisco (*) podemos pasar n valores y nos retorna tuplas
# con doble asterisco (*) podemos pasar n valores y nos retorna diccionarios

