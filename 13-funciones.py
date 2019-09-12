#!/usr/bin/env python3
"""Funciones en python"""

# Vamos a obtener el factorial de 5 sin usar una funcion
# Declaramos las variables
numero = 5
factorial = 1
# Declaramos ciclo iterador
while numero > 0:
    factorial = factorial * numero
    numero -= 1 # Realizamos un decremento al iterador
# Imprimimos el resultado
print(factorial)

# Print vacio para un output mas legible
print("")


# Para reusar el algoritmo n veces tendriamos que copiarlo nuevamente la cantidad de n veces que necesitemos usarlo
# una de las filosofias de python es "Dont repeat yourself" por ello usamos las funciones
# Las funciones nos permiten re usar las veces que queramos un algoritmo escribiendolo una sola vez

# Declaramos nuestra funcion para calcular el factorial
def factorial_numero():
    numero = 5
    factorial = 1
# Declaramos ciclo iterador
    while numero > 0:
        factorial = factorial * numero
        numero -= 1 # Realizamos un decremento al iterador
# Imprimimos el resultado
    print(factorial)

# Invocamos la funcion para que se ejecute
factorial_numero()


# Print vacio para un output mas legible
print("")


# Ahora nuestra funcipn recibira argumentos para operar con cualquier numero
def factorial_numero(numero): # lo que ponemos entre parentesis son los argumentos que debe recibir nuestra funcion para operar
    factorial = 1
# Declaramos ciclo iterador
    while numero > 0:
        factorial = factorial * numero
        numero -= 1 # Realizamos un decremento al iterador
# Imprimimos el resultado
    print(factorial)

# Invocamos nuestra funcion con algunos argumentos
factorial_numero(4)
factorial_numero(5)
factorial_numero(6)


# Print vacio para un output mas legible
print("")

# Podemos retornar cualquier valor en nuestra funcion para ser tomado por otra funcion o variable en el programa
def factorial_numero(numero): # lo que ponemos entre parentesis son los argumentos que debe recibir nuestra funcion para operar
    factorial = 1
# Declaramos ciclo iterador
    while numero > 0:
        factorial = factorial * numero
        numero -= 1 # Realizamos un decremento al iterador
# Imprimimos el resultado
    return factorial

resultado = factorial_numero(7)
print(resultado)


# Funciones mas complejas
# Definimos nuestra funcion
def suma(valor_uno, valor_dos, valor_tres): #Estamos pasando dos argumentos, cada argumento pasado se separa por coma (,)
    return valor_uno + valor_dos + valor_tres
resultado = suma(10,20,30) # Los valores son asigandos a la funcion acorde a las posiciones que se asignan, el valor 10 tomaria la posicion de valor_uno
print(resultado) # Imprimimos la variable
# Funcion para division
def division(valor_uno, valor_dos):
    return valor_uno / valor_dos #Retornamos la operacion
resultado = division(100,10) # Una nueva variable toma la variable retornada
print(resultado) # Imprimimos la variable

# Podemos intercambiar la posicion de los valores a pasar a la funcion de la siguiente manera
resultado = division( valor_dos = 10, valor_uno = 1 )
print(resultado)


# Nueva funcion para multiplicar
def multiplicacion(valor_uno, valor_dos):
    return valor_uno * valor_dos
resultado = multiplicacion(6,7)
print(resultado)

# Podemos pasar un solo valor
def multiplicacion2(valor_uno, valor_dos = 10):
    return valor_uno * valor_dos
resultado = multiplicacion2(6)
print(resultado)


# Podemos pasar funciones a otras funciones
def mostrar_resultado(funcion):
    print(funcion(6,8))

mi_variable = multiplicacion
mostrar_resultado( mi_variable )
