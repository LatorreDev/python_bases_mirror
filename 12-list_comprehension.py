#!/usr/bin/env python3
"""List Comprehension"""

# Este feature de python permite crear listas listas, diccionarios y tuplas de una manera muy sencilla
# Ejemplo, tener una lista con de 100 elementos con desde el numero 1 al 100
# Normalmente se haria de la siguiente manera:

# Se declara la lista
lista = []
# Se crea el ciclo iterador
for valor in range (0, 101): #Itera dentro de un rango determinado, en este caso 0 a 101
    lista.append(valor) # En cada iteracion, mediante el metodo append se va agregando el valor del iterador a la lista

# Se imprime la lista
print("la lista es", lista)
# Funciones print  vacias para hacer el output mas legible
print("")
print("")

# Con list comphehension se haria mas rapido de la siguiente manera
lista2 = [ valor for valor in range (0,101) ]   # El primer "valor" equivale a append, agrega el valor del iterador
                                                # A la lista
# Se imprime la lista
print("La lista 2 es:", lista2 )
# Funciones print  vacias para hacer el output mas legible
print("")
print("")

# Estructura de una list comprehension
# Valor a agregar a la lsita
# Un ciclo iterador

# Podemos agregar condicionales dentro de una lista comprehension
# Ejemplo, tener solo los numeros pares en una lista con rango de 0 a 100
# Declaramos una tercera lista con condicional anadido
lista3 = [valor for valor in range (0,101) if valor % 2 == 0]
# Se imprime la lista
print("La lista 3 es:", lista3 )
# Funciones print  vacias para hacer el output mas legible
print("")
print("")

# Ejemplo de list comprehension de tupla que contiene los numeros impares del 1 al 100
tupla = tuple( (valor for valor in range (0,101) if valor % 2 != 0 ) )
# Se imprime la tupla
print("La tupla es:", tupla)
# Funciones print  vacias para hacer el output mas legible
print("")
print("")

# Ejemplo de comprehension list con diccionario
diccionario = {indice:valor for indice, valor in enumerate(lista)} # Se indica el la llave y el valor en este caso indice y valor respectivamente
                                                                    # Se agrega el ciclo iterador y el objeto iterable, en este caso la lista llamada "lista"
# Se imprime el diccionario
print("El diccionario es:", diccionario)
# Funciones print  vacias para hacer el output mas legible
print("")
print("")
