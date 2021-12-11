"""
Date:       2021-11-12
Authors:    Jorge Luis Rodríguez Guzmán
File:       T1E1_pos_neg.py
Brief:      Ingresar un número y validar
            si es un número positivo, negativo o cero.
Score:      75
Version:    1.2.3
Fixes:      - PEP8 recomienda añadir espacios en blanco alrededor de
                los operadores
                
            [CORREGIDO] - Falta la condición de __main__
            
            [CORREGIDO] - PEP8 recomienda no dejar espacio en blanco 
                entre la condición de if y el carácter de dos puntos ':'
"""

if __name__ == "__main__":                        # PEP8
    num = float(input("Ingresa un número \n"))    # PEP8
    if num < 0:                                   # PEP8
        print(f"{num} es negativo ")
    if num > 0 :                                   # PEP8
        print(f"{num} es positivo ")
    if num == 0:                                  # PEP8
        print(f"{num} es neutro ")
