"""
Date:     2021-01-26
Authors:  Jorge Luis Rodríguez Guzmán
File:     T3E4_leap_year.py
Brief:    Este programa valida si una fecha es válida
Score:    90
Version:  1.2.3
Fixes:    
"""

if __name__ == "__main__":
       
    anio = 0
    mes = 0
    dia = 0
    
    repetir = True
       
    MESES = (
     "Enero", "Febrero",
     "Marzo", "Abril",
     "Mayo", "Junio",
     "Julio", "Agosto",
     "Septiembre", "Octubre",
     "Noviembre", "Diciembre"
    )
    
    MIN_ANIO = (1900,)
    MAX_MES = (12,)
    MIN_MES = (1,)
    OFFSET_MES_LISTA = (-1,) 
    MAX_DIAS = (31,)
    MIN_DIAS = (1,)
    FREQ_BISIESTA = (4,)
    NUM_DIAS_FEB_BIS = (28,)
    NUM_DIAS_FEB = (29,)
    NUM_DIAS_MES_IMPAR = (30,)
    FEBRERO = (2,)
    FREQ_PAR = (2,)
    MENSAJE_CUMPLEANIOS = ("Estas son las mañanitas ...")
     
     
    def validarFecha(dia,mes,anio,
                    max_dias,min_dias,
                    max_meses,min_meses,
                    frec_bis,num_dias_feb,
                    num_dias_feb_bis,febrero,
                    num_dias_impar,frec_par):
       if dia < min_dias:
           validacion = False
       else: 
           validacion = True
           
       if mes < min_meses:
           validacion = False
       
       if (mes % frec_par != 0) and (dia > num_dias_impar):
           validacion = False
               
       if (mes == febrero):
           if(anio % frec_bis == 0) and (dia > num_dias_feb_bis):
              validacion = False
           else:
               if (dia > num_dias_feb):
                   validacion = False
           
       
       return validacion
       
    def validarMaximo(valor,max_value):
       if (valor <= max_value or max_value == 0):
           return True
       else :
            
           return False
       
       
    while repetir:
        print('Se requiere una fecha \n ')
        cifraValidada = False
        while repetir and cifraValidada==False:
            dia = input("Escriba el día : ")
            dia = int(dia)
            cifraValidada = validarMaximo(dia,MAX_DIAS[0])
            if cifraValidada:
                print("\n \t\t\t :) \n")
                
            else:
                print("Escriba una cifra válida ")
            
                
            
        cifraValidada = False 
       
        while repetir and cifraValidada==False:
            mes = input("Escriba el mes : ")
            mes = int(mes)
            cifraValidada = validarMaximo(mes,MAX_MES[0])
            if cifraValidada:
                
                print("\n \t\t\t :) \n")
            else:
                print("Escriba una cifra válida ")
       
        cifraValidada = False 
        
        while repetir and cifraValidada==False:
            anio = input("Escriba el año : ")
            anio = int(anio)
            cifraValidada = validarMaximo(anio,0)
            if cifraValidada:
                
                print("\n \t\t\t :) \n")
            else:
                print("Escriba una cifra válida ")
       
        cifraValidada = False 
       
        if validarFecha(dia,mes,anio,
                        MAX_DIAS[0],MIN_DIAS[0],
                        MAX_MES[0],MIN_MES[0],
                        FREQ_BISIESTA[0],NUM_DIAS_FEB[0],
                        NUM_DIAS_FEB_BIS[0],FEBRERO[0],
                        NUM_DIAS_MES_IMPAR[0],FREQ_PAR[0]):
            print("La fecha "
                  f"{dia}-{MESES[mes+OFFSET_MES_LISTA[0]]}-{anio} "
                  " es correcta")
            repetir = False
        else:
            repetir = True
            print("La fecha "
                  f"{dia}-{MESES[mes+OFFSET_MES_LISTA[0]]}-{anio} "
                  " no existe,"
                  " intente de nuevo...\n")
           
     
     
     