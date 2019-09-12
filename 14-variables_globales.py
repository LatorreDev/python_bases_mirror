#!/usr/bin/env python3
"""Variables Globales en python 3"""

# Una declaracion de una variable que hagamos dentro de una funcion la conoceremos como variable local, y solo afectara lo que este dentro del contexto la funcion


# Definimos una funcion que detectara si una palabra es palindromo
def palindromo(frase):
    frase = frase.replace(' ','') # La funcion replace reemplaza un caracter que se pasa como primer argumento, por le caracter que se pasa como segundo argumento
                                 # frase es una variable local
    return frase == frase[::-1]

frase = 'anita lava la tina' # Esta variable frase es una variable global, se encuentra por fuera de cualquier funcion
                             # Puede ser accedida por cualquier funcion
print(frase) # Imprimimos unicamente lo que contiene la variable
resultado = palindromo(frase) # Pasamos la variable a una funcion
print(frase) # Imprimimos la nueva variable modificada por la funcion
print(resultado)

def valor_global():
    global variable_global # Esto modifica el valor de una variable global, se usa la palabra reservada global seguida de la variable global que vamos a modificar
    variable_global = 'Cambiar Valor' #Esto es una variable local

variable_global = 'Esto es una variable global'
print(variable_global)
valor_global()
print(variable_global)

# Las funciones tambien pueden crear variables globales
def crear_global():
    global nueva_variable
    nueva_variable = "Esto es una nueva variable global"

# Llamamos la funcion lo que ejecutara su codigo interno
crear_global()
#Imprimimos
print(nueva_variable)
