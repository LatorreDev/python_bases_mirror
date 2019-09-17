#!/usr/bin/env python3
"""Init en python 3"""

# Cuando queremos que los objetos que creamos se inicialicen con unos valores determinandos usamos el metodo init

# Definimos nuestra clase
class Lapiz:
# creamos nuestro init
    def __init__(self, color, contiene_borrador, usa_grafito): # Al metodo init le podemos pasar parametros
        self.color = color # Toma el valor que le es pasado como parametro al llamar la clase
        self.contiene_borrador = contiene_borrador
        self.usa_grafito = usa_grafito


    def dibujar(self):
        print("El lapiz esta dibujando")

    def borrar(self):
        if self.es_valido_para_borrar():
            print("El lapiz esta borrando")
        else:
            print("No es posible borrar")


    def es_valido_para_borrar(self):
        return self.contiene_borrador


lapiz_generico = Lapiz("Verde", True, True) # Le entregamos a nuestro nuevo objeto los parametros que definimos en el metodo init

lapiz_generico.dibujar()
lapiz_generico.borrar()
