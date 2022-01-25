"""
Date:       2021-11-26
Authors:    Jorge Luis Rodríguez Guzmán
File:       T2E2_number_list.py
Brief:      Este programa solicita al usuario
            que se introduzca un número entero
            el cual servirá de longitud para
            la introducción de una lista de elementos
Score:      85
Versión:    1.1.1
Fixes:      - Falto la captura en el README.md

            - En general esta bien solo que la conversion
            a enteros que solicite solo era castear a enteros
            int(value), ya que la funcion ord que usas retorna
            el valor UNICODE equivalente.

            - Trata de solo usar los espacios necesarios con el
            salto de linea, la terminal se puede volver un poco
            díficil de leer si los usas en exceso.
"""

if __name__ == "__main__":  
    #Inicialización de variables
    convertion = 0
    lista = []
    listaConvertida = [] 
    valorInicialEntero = 0
    n=0
    longitudNoValidada=True
    numeroDelElemento=1
    #Constantes
    OFFSET_USUARIO = 1
    BASE = 10
    contadorLetras=0
    DEFAULT_CONTADOR=0
    INCREMENTO_CONTADOR=1
    APAGAR_CICLO_CONSULTAS = 0
    
    while longitudNoValidada:
        
        n = int(input("Introduzca la longitud " 
                      "que desaa que tenga la lista \n"))
        if n<=0:
            print("El número debe ser mayor o igual que cero")
        else:
            
            for i in range(n):          
                lista.append(input(f"Introduzca el elemento número "
                                     f"{i+OFFSET_USUARIO} de la lista \n"))
                if i == n-1:
                    #1. Imprimir elementos y tipos de la lista
                    print(f"lista de elementos inicial: \n {lista}\n")
                    for k in range(n):
                        print(f"elemento numero {k+OFFSET_USUARIO}: \n"
                              f" valor: {lista[k]},"
                              f" tipo: {type(lista[k])}")    
                    #2. Cambiar el tipo de todos los elementos a int
                    for j in range(n):
                        listaConvertida.append(valorInicialEntero)
                        for l in str(lista[j]):
                            listaConvertida[j]+=ord(l)*BASE**contadorLetras
                            contadorLetras=+INCREMENTO_CONTADOR
                        contadorLetras=DEFAULT_CONTADOR
                    longitudNoValidada = False
                    
            """
            Con este ciclo while, 
            se solicita al usuario que introduzca números para 
            """
            while numeroDelElemento!=APAGAR_CICLO_CONSULTAS:
                numeroDelElemento = int(input("Introduzca el "
                                     "número del elemento "
                                     "que deseé consultar. \n\n"
                                     "Introduzca el 0 para terminar "
                                     "el programa o continúe consultando elementos \n\n\n"))
                if (numeroDelElemento)<=len(lista):
                    print(f"Elemento {numeroDelElemento} original : " 
                          f"{lista[numeroDelElemento-OFFSET_USUARIO]} \t "
                          f"Tipo : {type(lista[numeroDelElemento-OFFSET_USUARIO])}\n"
                          f"Elemento {numeroDelElemento} convertido a enteros : "
                          f"{listaConvertida[numeroDelElemento-OFFSET_USUARIO]} \t "
                          f"Tipo : {type(listaConvertida[numeroDelElemento-OFFSET_USUARIO])}"
                          "\n\n\n")
                else:
                    print(f"No hay más de {len(lista)} elementos")
            

            print(f"Lista original: \n {lista}\n\n"
                  f"Lista convertida: \n{listaConvertida} \n\n\n")

            #4.Ordenar los elementos
            lista.sort(key = str.lower)
            listaConvertida.sort()
            print(f"Lista original Ordenada: \n{lista}\n\n"
                  f"Lista convertida Ordenada: \n{listaConvertida}\n\n\n")
            
            #5.Invertir el orden de los elementos
 #           lista=lista.sort(reverse=True)
#            listaConvertida=listaConvertida.sort(reverse=True)
            lista.sort(reverse=True, key=str.lower)
            listaConvertida.sort(reverse=True)
            print(f"Lista original Invertida: \n{lista}\n\n"
                  f"Lista convertida Invertida: \n{listaConvertida}\n\n\n")


            
                
                
            
