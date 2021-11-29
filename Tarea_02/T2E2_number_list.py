"""
Date:       2021-11-26
Authors:    Jorge Luis Rodríguez Guzmán
File:       T2E2_number_list.py
Brief:      Este programa solicita al usuario 
            que se introduzca un número entero
            el cual servirá de longitud para 
            la introducción de una lista de elementos 
Score:      -
Versión:    0.0.1
Fixes:      -
"""

if __name__ == "__main__":  
    convertion = 0
    lista = []
    listaConvertida = [] 
    valorInicialEntero = 0
    n=0
    longitudNoValidada=True
    
    while longitudNoValidada:
        
        n = int(input("Introduzca la longitud " 
                      "que desaa que tenga la lista \n"))
        if n<=0:
            print("El número debe ser mayor o igual que cero")
        else:
            
            for i in range(n):          
                lista.append(input(f"Introduzca el elemento número "
                                     f"{i+1} de la lista \n"))
                if i == n-1:
                    #1. Imprimir elementos y tipos de la lista
                    print(f"lista de elementos inicial: \n {lista}\n")
                    for k in range(n):
                        print(f"elemento numero {k+1}: \n"
                              f" valor: {lista[k]},"
                              f" tipo: {type(lista[k])}")    
                    #2. Cambiar el tipo de todos los elementos a int
                    for j in range(n):
                        listaConvertida.append(valorInicialEntero)
                        for l in str(lista[j]):
                            listaConvertida[j]+=ord(l)                   
                    longitudNoValidada = False
            indiceElemento = 1-input("Introduzca el "
                                     "número de uno de los elementos")