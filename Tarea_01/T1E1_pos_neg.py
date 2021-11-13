"""
Date:       2021-11-12
Authors:    Jorge Luis Rodríguez Guzmán
File:       T1E1_pos_neg.py
Brief:      Ingresar un número y validar 
            si es un número positivo, negativo o cero.
Score:      -
Versión:    0.0.1
Fixes:      -
"""
num = int(input("Ingresa un número \n"))
if num < 0 :
    print (f"{num} es negativo ")
if num > 0 :
    print (f"{num} es positivo ")
if num == 0 :
    print (f"{num} es neutro ")
