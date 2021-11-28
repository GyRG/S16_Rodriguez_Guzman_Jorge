"""
Date:       2021-11-12
Authors:    Jorge Luis Rodríguez Guzmán
File:       T1E1_pos_neg.py
Brief:      Ingresar un número y validar
            si es un número positivo, negativo o cero.
Score:      65
Version:    0.1.2
Fixes:      - Falta la condición de __main__
            - PEP8 recomienda no dejar espacio en blanco entre la
                condición de if y el carácter de dos puntos ':'
"""

if __name__=="__main__":
    num=float(input("Ingresa un número \n"))
    if num<0:
        print(f"{num} es negativo ")
    if num>0:
        print(f"{num} es positivo ")
    if num==0:
        print(f"{num} es neutro ")
