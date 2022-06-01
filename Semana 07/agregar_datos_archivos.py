# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 10:58:00 2022

@author: USUARIO
"""

archivo = open("noticia.txt","at")
# \n -> para agrefar el contenido en una linea
contenido = "_\nFuente: RPP"

archivo.write(contenido)
archivo.close()