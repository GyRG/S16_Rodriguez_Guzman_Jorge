"""
Date:     2021-11-12
Authors:  Jorge Luis Rodríguez Guzmán
File:     T1E3_birthday.py
Brief:    Este programa solicita año, mes y día de cumpleaños 
          e implime el string 'Year:xxxx - Month:xx - Day: xx'
          con sus respectivos resultados
Score:    90
Version:  1.2.3
Fixes:    * Las "constantes" que sean 0 si se pueden poner 
               directamente en el código
               
          * Para constantes es mejor usar tuplas, ya que 
               son inmutables
          
          + Se que este ejercicio fue un poco ambigüo en 
               sus indicaciones, pero hiciste una buena 
               interpretación, +10 puntos
               
          - PEP8 recomienda no rebasar los 99 carácteres en una línea 
                de código, yo establecí en los requerimientos máximo 72
                carácteres (El conteo comienza desde el inicio de la 
                linea)
"""

if __name__ == "__main__":
     from datetime import datetime

     fechaActual = datetime.today().strftime('%m-%d')
     anioActual = datetime.today().strftime('%y')

     anio = 0
     mes = 0
     dia = 0

     MESES = (
          "Enero", "Febrero",
          "Marzo", "Abril",
          "Mayo", "Junio",
          "Julio", "Agosto",
          "Septiembre", "Octubre",
          "Noviembre", "Diciembre"
     )

     MAX_ANIO = int(anioActual) + 2000
     MIN_ANIO = (1900,)
     MAX_MES = (12,)
     MIN_MES = (0,)
     MAX_DIAS = (31,)
     MIN_DIAS = (0,)
     FREQ_BISIESTA = (4,)
     NUM_DIAS_FEB_BIS = (28,)
     NUM_DIAS_FEB = (29,)
     NUM_DIAS_MES_IMPAR = (30,)
     FEBRERO = (2,)
     FREQ_PAR = (2,)
     MENSAJE_CUMPLEANIOS = ("Estas son las mañanitas ...")

     while anio == 0:
          anio = int(input("Ingresa el año en el que naciste \n"))
          if ((anio <= MAX_ANIO) &
                  (anio >= MIN_ANIO[0])):
               print(f"Año : {anio} ")
          else:
               print("Es poco probable que hayas viajado "
                     "en el tiempo o que tengas "
                     f"{MAX_ANIO - MIN_ANIO[0]} años o mas")
               anio = 0

     while mes == 0:
          mes = int(input("Ingresa el número del mes en el que "
                          "naciste \n"))              # PEP8
          if ((mes <= MAX_MES[0]) &
                  (mes > MIN_MES[0])):
               print(f"Mes de : {MESES[mes - 1]}")
          else:
               print("Escríbelo con enteros del 1 al 12")
               mes = 0

     while dia == 0:
          dia = int(input("Ingresa el número de día en el que "
                          "naciste \n"))               # PEP8
          if (dia <= MAX_DIAS[0]) & (dia > MIN_DIAS[0]):
               if ((mes == FEBRERO[0]) &
                       (anio % FREQ_BISIESTA[0] == 0) &
                       (dia > NUM_DIAS_FEB_BIS[0])):
                    print(f"Recuerda que {MESES[mes - 1]} es "
                          "biciesto en el {anio}")      # PEP8
                    dia = 0
               else:
                    if ((mes % FREQ_PAR[0] != 0) &
                            (dia > NUM_DIAS_MES_IMPAR[0]) |
                            (mes == FEBRERO[0]) &
                            (dia > NUM_DIAS_FEB[0])):
                         print(f"Recuerda que {MESES[mes - 1]}"
                               " tiene menos días")         # PEP8
                         dia = 0
                    else:
                         print(f"Día : {dia} \n\n\n")
          else:
               print("Escríbelo correctamente")
               dia = 0
     if dia < 10:
         diaString = f"0{dia}"
     else:
         diaString= str(dia)
     if mes < 10:
         mesString = f"0{mes}"
     else:
         mesString = str(mes)
     fechaCumpleanios = str(f"{mesString}-{diaString}")

     print(f'Año : {anio}\nMes : {MESES[mes - 1]}\nDía : {dia}\n')

     # Este mensaje no se muestra cuando son días de un dígito
     if fechaCumpleanios == fechaActual:
          print(f"{MENSAJE_CUMPLEANIOS}")
