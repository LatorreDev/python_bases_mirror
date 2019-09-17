#!/usr/bin/env python3
"""Atributos y metodos en python 3"""

# Definimos nuestra clase
class Lapiz:
    color = "Amarillo"
    contiene_borrador = False
    usa_grafito = True

# Las caracteristicas que tiene clase se llaman atributos
# Las acciones que puede realizar se llaman metodos

# Creamos un metodo, estos deben estar dentro de la clase, notemos la identacion que tiene el siguiente metodo, esta dentro de la clase superior
    def dibujar(self):
        print("El lapiz esta dibujando")

    def borrar(self):
        if self.es_valido_para_borrar(): # Para llamar un metodo dentro de otro metodo igual usamos self
            print("El lapiz esta borrando")
        else:
            print("No es posible borrar")


    def es_valido_para_borrar(self):
        return self.contiene_borrador # Si llamamos a un atributo dentro de un metodo usamos self


# Creamos un nuevo objeto usando la clase declarada
lapiz_generico = Lapiz()

# Para llamar a nuestro objeto y su metodo lo hacemos de la siguiente manera
lapiz_generico.dibujar()
lapiz_generico.borrar()
lapiz_generico.contiene_borrador = True # Cambiamos el valor a un atributo
lapiz_generico.borrar()
