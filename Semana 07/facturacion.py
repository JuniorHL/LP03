# -*- coding: utf-8 -*-
"""
Created on Wed Jun  1 08:47:00 2022

@author: USUARIO
"""

# Dado el subtotal, calcular el IGV y el total

import financieros
subtotal = 800.77
print(f"Subtotal: {subtotal}")
print(f"IGV: {financieros.obtenerIGVSubtotal(subtotal): .2f}")
print(f"Total: {financieros.obtenerTotalconSubtotal(subtotal): .2f}")