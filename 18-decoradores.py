#!/usr/bin/env python3
"""Decoradores"""

# Un decorador nos permite agregar mayor funcionalidad a una funcion ya creada
# Un decorador es una funcion que recibe como parametro otra funcion y retorna una nueva funcion

# A, B, C son funciones
# A recibe como parametro B para poder crear C

# declaramos una funcion sencilla
def saluda():
    print("Hola mundo")

# Llamamos nuestra funcion
saluda()

# Como creamos el decorador
def decorador(is_valid = True): #Los decoradores pueden recibir parametro
    def _decorador(func): #A, B

        def before_action():
            print("Vamos a ejecutar la funcion")

        def after_action():
            print("La funcion se ejecuto")

        def nueva_funcion(*args, **kwargs): # Recibe N cantidad de argumentos
            if is_valid:
                before_action()

            resultado = func(*args, **kwargs) # Ejecuto la funcion

            after_action()
            return resultado
        return nueva_funcion #C

    return _decorador


@decorador() # Tiene el nombre de nuestra funcion decoradora
def suma(num_uno, num_dos):
    return num_uno + num_dos

resultado = suma(80, 17)
print(resultado)

# Los decoradores tambien pueden recibir parametros
# Si se envia como parametro una funcion, es por que se necesita anadirle mas funcionalidad a esa funcion
