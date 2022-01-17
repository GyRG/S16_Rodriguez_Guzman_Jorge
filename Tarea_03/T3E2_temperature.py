# -*- coding: utf-8 -*-
"""
Date:       2021-11-26
Authors:    Jorge Luis Rodríguez Guzmán
File:       T3E2_temperature.py
Brief:      Este programa contiene dos funciones 
            una convierte temperaturas de C° a F°
            y la otra de F° a C°
Score:      -
Versión:    0.0.1
Fixes:      -
"""
if __name__ == "__main__":
    factor = (5/9,9/5)
    suelo = (32.0,)
    opciones = 3
    minConversiones = (1,)
    maxConversiones = (2,)
    def farenheit_celcius(grados):
        """
        Esta función recibe un valor de temperatura 
        en grados farenheit
        :returns: el valor en grados Celcius
        """
        grados = (grados - suelo[0]) * factor[0]
         
        return grados
    
    def celcius_farenheit(grados):
        """
        Esta función recibe un valor de temperatura 
        en grados Celcius
        :returns: el valor en grados Farenheit
        """
        grados = (grados * factor[1]) + suelo[0]
        return grados
    
    
    while opciones != 0:
            opciones = int(input("Elija la conversión que desee hacer \n"
                        "Farenheit a Celcius -> 1 \n"
                        "Celcius a Farenheit -> 2 \n"
                        "Terminar el proceso -> 0 \n"))
            
            if (opciones >= minConversiones[0]) and (opciones <= maxConversiones[0]):
                if opciones == 1:
                    grados = float(input("Escriba el valor "
                                         "en grados Farenheit: "))
                    print(f'{grados} F° es igual '
                          f'a {farenheit_celcius(grados)} C° \n')
                if opciones == 2:
                    grados = float(input("Escriba el valor "
                                         "en grados Celcius: "))
                    print(f'{grados} C° es igual '
                          f'a {celcius_farenheit(grados)} F° \n')
                
                continuar = input('¿desea continuar? -> s : ')
                if 's' != continuar:
                    opciones = 0
            else:
                opciones = 0 
                