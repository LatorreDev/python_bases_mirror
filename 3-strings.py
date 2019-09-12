#!/usr/bin/env python3
"""Strings in python"""
# Para declarar el valor de una variable tipo string se debe declarar entre comillas dobles o sencillas
# Se declara variable de tipo string
my_string = "Hola Mundo!"
# Se imprime la variable
print (my_string)
# Si se declara el string con comillas dobles se pueden anadir comillas dobles dentro de la declaracion
my_string = "Hola Mundo!" 'David'
# Se imprime la variable
print (my_string)
# Strings con saltos de linea
my_string = ''' Este es un string con saltos de linea
                usando comillas sencillas'''
# Se imprime la variable
print (my_string)
# String con saltos de linea comunes \n
my_string = "Este es un string con saltos de linea\nusando backslash n" 
# Se imprime la variable
print (my_string)
# Concatenar strings
# Se declaran nuevas variables de tipo string
course = "Python 3"
name = "David"

# Se concatenan las variables
final_message = "Nuevo curso de "+ course + " por " + name
# Se imprime la concatenacion
print(final_message)
# Otra manera de imprimir
final_message = "Nuevo curso de %s por %s" %(course, name)
# Se imprime la concatenacion
print(final_message)
# Otra manera de imprimir
final_message = "Nuevo curso de {} por {}".format(course, name)
# Se imprime la concatenacion
print(final_message)
