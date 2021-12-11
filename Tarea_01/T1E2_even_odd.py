"""
Date:       2021-11-12
Authors:    Jorge Luis Rodríguez Guzmán
File:       T1E2_even_odd.py
Brief:      Ingresar un número y validar si es par o impar.
Score:      85
Versión:    1.1.2
Fixes:      - Falta la condición de __main__

            - PEP8 recomienda añadir espacios en blanco alrededor de
                los operadores 
"""

# BIEN DECLARADO LAS CONSTANTES A COMO SE ESPECIFICÓ EN LOS REQUISITOS
# PERO ES MEJOR USAR TUPLAS
if __name__ == '__main__':
    FREQ = (2,)
    MODULO_ESPERADO = (0,)
    
    num = int(input("Ingresar un número: \n"))    # PEP8
    # SERIA BUENO VALIDAR E INDICAR CUANDO EL NÚMERO SEA CERO
    if num != 0:
        if num % FREQ[0] != MODULO_ESPERADO[0]:             # PEP8 PEP8
            print(f"{num} es impar")
        else:
            print(f"{num} es par")
    else:
        print(f"{num} es simplemente cero")
