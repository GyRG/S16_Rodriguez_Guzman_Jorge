# -*- coding: utf-8 -*-
"""
Date:       2021-11-26
Authors:    Jorge Luis Rodríguez Guzmán
File:       T3E3_arithmetic.py
Brief:      Este programa realiza operaciones aritméticas 
            con los números que se le introducen
Score:      -
Versión:    0.0.1
Fixes:      -
"""
if __name__ == "__main__":

    opciones = 5
    minOperaciones = (1,)
    maxOperaciones= (4,)
    def suma(num1, num2):
        """
        Esta función recibe dos números y los suma
        :returns: resultado de la operación
        """
        return num1 + num2
    def resta(num1, num2):
        """
        Esta función recibe dos números y los resta
        :returns: resultado de la operación
        """
        return num1 - num2
    def multiplicacion(num1, num2):
        """
        Esta función recibe dos números y los multiplica
        :returns: resultado de la operación
        """
        return num1 * num2
    def division(num1, num2):
        """
        Esta función recibe dos números y los divide
        :returns: resultado de la operación
        """
        return num1 / num2
         
    
    
    while opciones != 0:
            opciones = int(input("Elija la conversión que desee hacer \n"
                        "Suma -> 1 \n"
                        "Resta -> 2 \n"
                        "Multiplicación -> 3 \n"
                        "División -> 4 \n"
                        "Terminar el proceso -> 0\n"))
            
            if (opciones >= minOperaciones[0]) and (opciones <= maxOperaciones[0]):
                
                if opciones == 1:
                    num1 = float(input("Escriba el primer valor: "))
                    num2 = float(input("Escriba el segundo valor: "))
                    print(f'{num1} mas {num2} es igual a '
                          f'{suma(num1,num2)}')
                if opciones == 2:
                    num1 = float(input("Escriba el primer valor: "))
                    num2 = float(input("Escriba el segundo valor: "))
                    print(f'{num1} menos {num2} es igual a '
                          f'{resta(num1,num2)}')
                if opciones == 3:
                    num1 = float(input("Escriba el primer valor: "))
                    num2 = float(input("Escriba el segundo valor: "))
                    print(f'{num1} por {num2} es igual a '
                          f'{multiplicacion(num1,num2)}')
                if opciones == 4:
                    num1 = float(input("Escriba el dividendo: "))
                    num2 = float(input("Escriba el divisor: "))
                    print(f'{num1} entre {num2} es igual a '
                          f'{division(num1,num2)}')
                    
                continuar = input('¿desea continuar? -> s : ')
                if 's' != continuar:
                    opciones = 0
            else:
                opciones = 0 
                