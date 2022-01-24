"""
Date:       2022-01-21
Authors:    Jorge Luis Rodríguez Guzmán
File:       T5E1_RegEx.py
Brief:      Este programa permite hacer validaciones 
            de correo electrónico,números telefónicos
            y CURPS
            
Score:      -
Versión:    0.0.1
Fixes:      -
"""

from Tarea_05.funciones_validacion.validaciones import *

if __name__ == "__main__":
    
    cuentas = {
        "Jorge317":"jorge@correo",
        "Asimov":"isa@casim.org",
        "Lovelance":"ada.com"}
    
    for usuario, correo in cuentas.items():    
        
        validacion = validarCorreoElectronico(correo)
        print(validacion)
        
        #validacion = (usuario+validarCorreoElectronico(correo).string())
        #if validacion:
         #   print (usuario+" no validado")
        
    
    
    validarNumeroTelefonico("(001)1553110")
    validarNumeroTelefonico("0011553110")
    validarNumeroTelefonico("001-155-3110")
    
    validarCurp("ROGUGL342501PMSRMG05")
