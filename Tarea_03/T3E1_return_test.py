# -*- coding: utf-8 -*-
"""
Date:       2021-01-16
Authors:    Jorge Luis Rodríguez Guzmán
File:       T3E1.py
Brief:      Este programa declara una función que pide un número 
            y regresa un string mostrando el número introducido 
Score:      -
Versión:    0.0.1
Fixes:      -
"""

if __name__ == "__main__":
    
    def imprimirNumero():
        """
        Esta función solicita un número
        :returns: Un string con el número solicitado
        """
        numero = (str(input("Introduzca un número: ")))
        numero = f'El número es el {numero}'
        return numero
    
    print(imprimirNumero())
    
    help(imprimirNumero)