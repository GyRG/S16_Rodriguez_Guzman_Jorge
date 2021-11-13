"""
Date:       2021-11-12
Authors:    Jorge Luis Rodríguez Guzmán
File:       T1E3_birthday.py
Brief:      Este programa solicita año, mes y día de cumpleaños 
            e implime el string 'Year:xxxx - Month:xx - Day: xx'
            con sus respectivos resultados
Score:      -
Versión:    0.0.1
Fixes:      -
"""
from datetime import datetime

fechaActual = datetime.today().strftime('%m-%d')

anio = 0
mes = 0
dia = 0

MESES = [
    "Enero","Febrero",
    "Marzo", "Abril",
    "Mayo","Junio",
    "Julio","Agosto",
    "Septiembre","Octubre",
    "Noviembre", "Diciembre"
    ]

MAX_ANIO = 2021
MIN_ANIO = 1900
MAX_MES = 12
MIN_MES = 0
MAX_DIAS = 31
MIN_DIAS = 0
FREQ_BISIESTA = 4
NUM_DIAS_FEB_BIS = 28
NUM_DIAS_FEB = 29
NUM_DIAS_MES_IMPAR =30
ANIO_DEFAULT = 0
MES_DEFAULT = 0
DIA_DEFAULT = 0
FEBRERO = 2
FREQ_PAR = 2
RESULTADO_MODULO = 0
MENSAJE_CUMPLEANIOS = "Estas son las mañanitas ..."



while anio ==  ANIO_DEFAULT :
    anio = int(input("Ingresa el año en el que naciste \n"))
    if (anio <= MAX_ANIO) & (anio >= MIN_ANIO) :
        print(f"Año : {anio} ")
    else :
        print("Es poco probable que hayas viajado "  
              "en el tiempo o vivas más de 120 años")
        anio = ANIO_DEFAULT
        
while mes == MES_DEFAULT :
    mes = int(input("Ingresa el número del mes en el que naciste \n"))
    if (mes<=MAX_MES)&(mes>MIN_MES):
        print(f"Mes de : {MESES[mes-1]}")
    else :
        print("Escríbelo con enteros del 1 al 12")
        mes = MES_DEFAULT
    
while dia == DIA_DEFAULT :
    dia = int(input("Ingresa el número de día en el que naciste \n"))
    if (dia<=MAX_DIAS)&(dia>MIN_DIAS):
        if (mes == FEBRERO) & (anio%FREQ_BISIESTA == RESULTADO_MODULO ) & (dia>NUM_DIAS_FEB_BIS):
            print(f"Recuerda que {MESES[mes-1]} es biciesto en el {anio}")
            dia = DIA_DEFAULT
        else :
            if (mes%FREQ_PAR!=RESULTADO_MODULO)&(dia>NUM_DIAS_MES_IMPAR) | (mes==FEBRERO) & (dia>NUM_DIAS_FEB):
                print(f"Recuerda que {MESES[mes-1]} tiene menos días")
                dia = DIA_DEFAULT
            else :
                print(f"Día : {dia} \n\n\n")
    else :
        print("Escríbelo correctamente")
        dia = DIA_DEFAULT
        
fechaCumpleanios = str(f"{mes}-{dia}") 


print(f'Año : {anio}\nMes : {MESES[mes-1]}\nDía : {dia}\n')
  
if fechaCumpleanios == fechaActual :
    print(f"{MENSAJE_CUMPLEANIOS}")
