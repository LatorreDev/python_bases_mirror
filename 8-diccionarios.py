#!/usr/bin/env python3
"""Estudio sobre diccionarios"""
# Los diccionarios son estructuras de datos similares a las listas y las tuplas
# Nos permite almacenar datos tales como, strings, enteros, booleanos, etc.
# Los diccionarios pueden almacenas tambien lista o tupla, inclusive otros diccionarios
# La diferencia con una lista, es que un diccionario no se rige por un indice, los diccionarios
# se modifican por medio de una clave o key

# Declaramos el diccionario
dictionary = { 'a' : 55} # El valor 55 tiene como clave el caracter a
# Imprimimos el diccionario
print(dictionary)
# las claves pueden ser strings, enteros o tuplas
dictionary_2 = { 'a' : 55, 5: "Esto es un string", (1,2) : False }
# Imprimimos el nuevo diccionario
print(dictionary_2)


# Si dos claves son iguales, el diccionario toma la ultima clave
same_key = {'a' : 100, 'a' : 200}
# Se imprime el diccionario
print(same_key)


# Los diccionarios pueden crecer o decrecer


# Podemos anadir un valor a un diccionario de la siguiente manera
dictionary_2['c'] = "Nuevo String" # Pasamos el nombre del diccionario, entre parentesis cuadrado su clave y su valor precedido de un signo de =
# Imprimimos el diccionario
print(dictionary_2)


# Podemos modificar un valor de la misma manera como anadimos un nuevo valor, pero en el campo de la clave, pasamos la clave a modificar
dictionary_2['a'] = 300
# Imprimimos el nuevo diccionario
print(dictionary_2)


# Para obtener los datos de un diccionario se puede hacer de la siguiente manera
valor = dictionary_2[5] # Le pasamos el diccionario y la clave, esto accedera por medio de ella al valor almacenado relacionado con dicha clave
# imprimimos la variable valor
print(valor)


# Para evitar errores al intentar obtener un valor con una clave no existente podemos usar el metodo get
# get recibe como primer parametro la llave, como segundo parametro lo que queremos que retorne si no encuentra el parametro
valor = dictionary_2.get('z', "La clave no existe") # El parametro que retorna, puede ser un string, booleano, entero, etc
#imprimimos la nueva variable
print(valor)


# Para eliminar un elemento del diccionario usamos la palabra reservada del psando como parametro al diccionario la clave
del dictionary_2[5]
# Imprimimos el nuevo diccionario
print(dictionary_2)


# Algunas veces solo necesitamos las claves o los valores de un diccionarios
# para obtener solo las llaves lo podemos hacer con el metodo keys
my_keys = dictionary_2.keys()
# imprimimos la variable que prteviamente declaramos
print(my_keys)
# Podemos pasar las claves obtenidas a una lista para poder trabajar con ellas de la siguiente manera
my_keys = list(dictionary_2.keys())
# imprimimos la variable para verificar el output
print(my_keys)


# Para obtener los valores del diccionario utilizamos el metodo values
my_values = list(dictionary_2.values())
# Imprimimos la variable
print (my_values)


# Si lo que queremos es trabajar con una tupla en vez de una lista al obtener las claves o valores de un diccionario
# reemplazamos list por tuple


# Para extender un diccionario
# Declaramos un nuevo diccionario con sus claves y llaves
concat_dict = { 'z' : 23, 'w' : 88 }
# Concatenamos los diccionarios con el metodo update
dictionary_2.update(concat_dict)
# Imprimimos el diccionario para verificar
print(dictionary_2)
