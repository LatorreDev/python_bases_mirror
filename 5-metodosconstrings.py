#!/usr/bin/env python3
"""Metodos de strings"""

"""Formato"""

# Se declara las variables de tipo string
course = "curso"
my_string = "codigo facilito!"
# Nueva variable concatenandolas
result = "{} de {}".format(course, my_string)
# Se imprime la nueva variable
print(result)
# Nueva variable concatenandolas
result = "{a} de {b}".format(a=course, b=my_string)
# Se imprime la nueva variable
print(result)
# Metodo lower, toma el string y crea uno nuevo con todas las letras en minusculas
result = result.lower()
# Se imprime
print(result)
# Metodo upper, crea el nuevo string con todas las letras en mayusculas
result = result.upper()
# Se imprime
print(result)
# Metodo Title, crea un nuevo string como titulo
result = result.title()
# Se imprime
print(result)

"""Busqueda"""

# Nueva variable con metodo de busqueda
pos = result.find('codigo')
# Se imprime la variable
print(pos)
# Metodo de contado de un caracter o numero dentro de un string
count = result.count('c')
# Se imprime la variable
print(count)

""""Sustitucion"""
# Metodo para reemplazar un caracter con otro, es case sensitive
new_string = result.replace('c', 'x')
# Se imprime la variable
print(new_string)
# Metodo para separar una lista (split) acorde a un criterio
new_string = result.split(' ') # En este caso esta seccionado por espacios
# Se imprime la variable
print (new_string)
