#!/usr/bin/env python3
"""Clases y objetos en python 3"""

# Programacion orientada a objetos (paradigma de programacion)

# Un objeto en su analogia con la realidad es igual a cualquier objeto, como un lapiz o un borrador
# Lo que diferencia un lapiz de otro es su tamano, calidad, color, textura, etc
# un lapiz puede realizar ciertas cosas como escribir

# Un objeto tiene caracteristicas y puede realizar acciones
# Podemos tener un lapiz de colegio y un lapiz profesional de dibujo
# un lapiz profesional se diferencia del generico del colegio en su calidad del grafito
# calidad de la madera, etc.

# Pero si retiramos todas las caracteristicas que los diferenica, nos quedaria "la plantilla"
# de lo que es un lapiz, las bases genericas para que un lapiz sea considerado como tal.
# La plantilla en programacion se llama clase y nos permite crear n cantidad de objetos

# EN PYTHON TODO ES UN OBJETO

# Vamos a ver como se crea una clase con el ejemplo de lapiz
# usamos la palabra reservada class
class Lapiz: # Una clase siempre empieza en mayuscula y si tiene dos palabras se usa camel case, como LapizDibujo
    color = "Amarillo"
    contiene_borrador = False
    usa_grafito = True
# asi queda definida nuestra plantilla o clase

# Creamos un nuevo objeto con base en la clase que creamos
lapiz_generico = Lapiz()
print(lapiz_generico.color) # De esta manera verificamos el atributo color de nuestro lapiz generico que en este caso sera amarillo
