#!/usr/bin/env python3
"""Ciclos while"""

# Se utiliza cuando no sepamos cuantas iteraciones del ciclo se va a realizar
# un while se declara de la siguiente manera
# while condicion:
#   codigo
# else:
#   codigo
# El else no es necesario para declarar un while
# se pueden usar operadores de comparacion como > >= < <= == !=
# UN WHILE SIEMPRE DEBE ESTAR LIMITADO, SINO QUEDARA INFINITO

# Declaramos la variable que sera nuestro contador y le asignamos su valor
contador = 0

#Declaramos un while
while contador < 10:
    print(contador)
    contador +=1 #Aumenta el contador en 1
else:
    print("el while ha terminado")


# Se reasigna el contador a 0
contador = 0

# Se pueden combinar con otros condicionales
while contador < 10:
    print(contador)
    contador +=1

    if contador == 5:
        print("Estamos a la mitad!")
else:
    print("el while ha terminado!")


# Los whiles tienen palabras reservadas como continue o break
# continue, si la condicion se cumple continua la ejecucion
# break, si se cumple la condicion, se rompe el ciclo

# Se reasigna el contador a 0
contador = 0

while contador < 10:
    print(contador)
    contador +=1

    if contador == 5:
        continue
    if contador == 6:
        break
else:
    print("El ciclo ha terminado!")
