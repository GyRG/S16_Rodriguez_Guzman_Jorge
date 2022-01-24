import re 

def validarCorreoElectronico(correo):
    validacion = re.search("@",correo)
    if validacion:
        validacion = correo
    else: 
        validacion = correo
    return validacion

def validarNumeroTelefonico(numero):
    return numero    

def validarCurp(curp):
    return curp
