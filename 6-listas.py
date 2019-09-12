#!/usr/bin/env python3
"""Listas en Python"""
# Son un tipo de dato que a diferencia de strings y enteros puede almacenar diferentes tipos de datos
# Pueden aumentar su tamano
# Cada vez que usamos [] estamos trabajando con listas
# Pueden almacenar strings, enteros, flotantes, booleanos

# Definimos una lista
my_list = ["string", 15, 15.6, True]
# Podemos anadir elementos al final de la lista con el metodo append
my_list.append(6)
# Se imprime la lista 
print(my_list)
# Podemos anadir elementos en cualquier parte de la lista especificando su posicion y su valor
my_list.insert(1, "insert")
# Imprimimos la posicion de la lista
print(my_list[1])
# Podemos remover elementos por su valor dentro de la lista
my_list.remove(15)
# Imprimimos la lista
print(my_list)
# Las listas se pueden tratar como pilas, con el metodo pop, que elimina el ultimo elemento de la lista
last_value = my_list.pop()
print(last_value)
# Podemos ordenar listas de enteros
# Definimos una lista de enteros
int_list = [3,4,7,8,6,1,2,9,0,5]
# Imprimimos la nueva lista
print(int_list)
# Ordenamos la lista de forma ascendente con el metodo sort
int_list.sort()
# Imprimimos la lista ordenada
print(int_list)
# Podemos ordenar en orden descendente
int_list.sort(reverse = True)
# Imprimimos la lista
int_list
# Podemos concatenar listas
# Declaramos una segunda lista que contenga solo enteros
int_list_2 = [10,11,12]
# Concatenamos las dos listas con el metodo extend, pasando como parametro la lista a anadir
int_list.extend(int_list_2)
# Imprimimos la lista concatenada
print(int_list)
# Si concatenamos las listas con el metodo append, este crearia una sublista dentro de la primera lista
int_list.append(int_list_2)
# Imprimimos la lista concatenada y verificamos su output
print(int_list)
