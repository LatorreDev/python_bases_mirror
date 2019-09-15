#!/usr/bin/env python3
"""Lambdas en python 3"""

# Las funciones lambda son funciones anonimas que son de una sola linea de codigo
# Estas funciones son sobre demanda, se ejecutan depende de las condiciones de nuestro programa

# Una funcion normla es asi
def suma(valor_uno, valor_dos):
    return valor_uno + valor_dos

resultado = suma(10, 20)
print(resultado)

# Con lambda es asi

mi_funcion = lambda valor_uno, valor_dos : valor_uno + valor_dos
# Se utiliza la palabra reservada lambda, los argumentos a pasar sin parentesis, dos puntos (:) y lo que se requiere operar
# En este caso sumar dos numeros

resultado = suma(10, 20)
print(resultado)

# Otra lambda
formato = lambda sentencia : '¿{}?'.format(sentencia)
resultado = formato('Puedes convertir esto en una pregunta')
print(resultado)

# Si una lambda no recibe ningun valor
no_valor = lambda : 10 #No recibe ningun valor, pero retorna lo que haya despues de los dos puntos (:)
resultado = no_valor() # La funcion no esta recibiendo nada
print(resultado)

# Las funciones lambda deben ser lo mas simple posible
