# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:47:18 2022

@author: USUARIO
"""

archivo = open("archivo de prueba.txt","wt")
contenido = "Linea1 Hola amigos ¿Como están? \nLinea2 Bienvenidos a la Untels. "
archivo.write(contenido)
archivo.close()