# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 09:37:06 2022

@author: USUARIO
"""
# Importamos la libreria

import camelcase

# Tenemos una cadena llamada nombre y se desea
# que se muestre en formato titulo
nombre = "anselmo Junior Huancas leuyacc"

print(nombre.upper())
print(nombre.title())

# Creamos un objeto llamado cam
cam = camelcase.CamelCase()
print("Con Camelcase...")

# Imprimimos el nombre en formato titulo
# Utilizamos camelcase
print(cam.hump(nombre))

# Para resolver el problema
# Creamos otro objeto cam2
# Al definir el objeto, incluimos los argumentos
# "anselmo" - "leuyacc"

cam02 = camelcase.CamelCase('anselmo','leuyacc')
print(cam02.hump(nombre))
