"""
Date:       2021-11-12
Authors:    Jorge Luis Rodríguez Guzmán
File:       T1E2_even_odd.py
Brief:      Ingresar un número y validar si es par o impar.
Score:      -
Versión:    0.0.2
Fixes:      -
 """
FREQ = 2
MODULO_ESPERADO = 0

num=int(input("Ingresar un número: \n"))
if num%FREQ!=MODULO_ESPERADO:
    print(f"{num} es impar")
else:
    print(f"{num} es par")
