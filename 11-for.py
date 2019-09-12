#!/usr/bin/env python3
"""Ciclo For"""

# El ciclo for se usa cuando sepamos cuantas iteraciones se van a realizar
# Nos permite iterar tuplas, listas, strings o diccionarios

# Declaramos una lista de enteros
lista = [1,2,3,4,5,6,7,8,9,10]

# Los ciclos for se declaran de la siguiente manera

for valor in lista: #valor seria nuestra variable iteradora, aca se inicializa automaticamente en 0
    print(valor)

# Los ciclos for tambien pueden tener un rango (limite desde el cual se ejecuta hasta donde va a terminar)
nuevo_rango = range(10,20) # Primer parametro indica el inicio, y segundo parametro al finalizacion.
for valor in nuevo_rango:
    print(valor)


# Tres paramentros en un rango indicaria que habrian ciertos saltos en la iteracion
for valor in range(0,20,4): # Inicia en 0, termina en 20 y cumple la condicion cada 4 iteraciones, en este caso imprimir
    print(valor)

# Para obtener el indice lo podemos hacer de la siguiente manera
# Declaramos una variable que sera nuestro indice
indice = 0
# Re inicializamos nuestra variable valor en 0
valor = 0
# Declaramos nuestro ciclo for
for valor in lista:
    print(valor, "tiene el indice", indice)
    indice +=1 # Incrementamos nuestro indice en 1, igual que un ciclo while


# Si no queremos apoyarnos en una variable fuera del ciclo podemos usar la funcion enumerate
# Re inicializamos nuestra variable valor en 0
valor = 0
# Declaramos nuestro ciclo for con la funcion enumerate
for indice, valor in enumerate(lista):
    print(valor, "tiene el valor", indice)


# Para obtener el unicamente el tamano de la lista usamos la funcion len
# imprimimos la lista dentro de la funcion len
print("el tamano de la lista es:", len(lista))


# Los strings y dicccionarios son iterables, los enteros no.
# Para iterar un diccionario usamos el metodo items
# Declaramos un diccionario
dictionary = {'a' : 10, 'b' : 20, 'c' : 30}
# Iteramos el diccionario
for key, value in dictionary.items(): # Los parametros que se pasan son la llave y el valor que guarda, en este caso, key y value respectivamente
    print("La llave es", key, "tiene valor de", value)
