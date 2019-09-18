#!/usr/bin/env python3
""" Paquetes en Python """

# Un paquete no es mas que una carpeta el cual va a contener todos los modulos que necesitos
# Los modulos no son mas que archivos de extension .py

# Para que el interprete de python reconozca nuestra carpeta como un paquete debe contener un archivo de nombre __init__.py

# Para este ejemplo se crea la carpeta animals

# La carpeta de un paquete tiene una estructura de
# Carpeta
# Archivo init
# Los modulos que lo componen

from animals.gato import Gato

gato = Gato('Nuevo gato por paquete')
print(gato.nombre)
