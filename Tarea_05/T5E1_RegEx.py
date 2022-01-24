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
    
    ex_reg_email = ''
    ex_reg_phone = ''
    ex_reg_CURP = ''

    cuentas = {
        "Jorge317":"jorge@correo",
        "Asimov":"isa@casim.org",
        "Lovelance":"ada.com"}
    
    for usuario, correo in cuentas.items():    
        
        validacion = validarData(correo,ex_reg_email)
        print(usuario+" : "+validacion+"\n")
        
    telefonos = [
        '(001)1553110',
        '0011553110',
        '001-155-3110']
    
    for telefono in telefonos:
        validacion = validarData(telefono,ex_reg_phone)
        print(telefono+" : "+validacion+"\n")
        
    curps = ['MLGL990501PMSRMG05',
             'ROGJ930907HGTDZR02',
             'KMR671204MLRGZ90']
    
        
    for curp in curps:
        validacion = validarData(curp,ex_reg_CURP)
        print(curp+" : "+validacion+"\n")
        
    
    
