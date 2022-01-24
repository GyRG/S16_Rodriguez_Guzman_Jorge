import re 
def validarData(data,ex_reg):
    validacion = re.search(
        ex_reg,
        data, 
        re.IGNORECASE)
    
    if validacion:
        veredicto = "Datos válidos"
    else: 
        veredicto = "Datos no validos"
        
    return veredicto
