#!/usr/bin/env python3
"""Condicionales en python"""


# Creamos una variable de tipo string y le asignamos su valor
fruta = "kiwi"

# Creamos el condicional if, esta es su estructura
# if condicion:
#   codigo
# Hay que tener especial cuidado con la identacion, ya que en python no se usan llaves para encerrar bloques de codigo

if fruta == "kiwi":
    print("El valor es kiwi")
else: # El else es el bloque de codigo que se ejecuta si no se cumple la condicion
    print("No son iguales")

# Los if se pueden hacer en una sola linea

msg = "El valor es kiwi" if fruta == "kiwi" else "Los valores no son inguales"
# Imprimimos
print(msg)

# para evaluar varias condiciones usamos la palabra reservada elif
# cambiamos el valor de la variable
fruta = "manzana"
# creamos el if con multi condicion
if fruta == "kiwi":
    print("Es un kiwi")
elif fruta == "manzana":
    print("Es una manzana")
else:
    pass # la palabra reservada pass sirve para omitir la ejecucion de una operacion que deberia retornar, pero queremos omitir cuando se cumpla.


# En python todas nuestras variables son booleanas (True or False)
# True = 1
# False = 0
# Todas las variables vacias o nulas son falsas [], (), {}, 0, '', None
# Todas las variables que tengan algun valor son verdaderos
if []:
    print("Es verdadero")
else:
    print("Es Falso")

# Con los condicionales deben tenerse en cuenta la tabla de verdad, ya que al concatenar con operadores logicos, podemos tener condicionales
# mas complejos
