"""
Date:       2021-11-12
Authors:    Jorge Luis Rodríguez Guzmán
File:       T1E1_pos_neg.py
Brief:      Ingresar un número y validar
            si es un número positivo, negativo o cero.
Score:      65
Version:    0.1.1
Fixes:      - Falta la condición de __main__

            - PEP8 recomienda no dejar espacio en blanco entre la
                condición de if y el carácter de dos puntos ':'

            - PEP8 recomienda no dejar espacio en blanco entre printf
                y la apertura del paréntesis '('
"""

# Sería mejor castear a float para hacer el programa más versátil
num = int(input("Ingresa un número \n"))        
if num < 0 :                                    # PEP8
    print (f"{num} es negativo ")               # PEP8                           
if num > 0 :                                    # PEP8
    print (f"{num} es positivo ")               # PEP8
if num == 0 :                                   # PEP8
    print (f"{num} es neutro ")                 # PEP8
