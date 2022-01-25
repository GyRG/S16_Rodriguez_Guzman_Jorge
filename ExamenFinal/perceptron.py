"""
Date:       2022-01-23
Authors:    Jorge Luis Rodríguez Guzmán
File:       perceptron.py
Brief:      Este es el código con el que se resuelven
            los ejercicios 3, 4 y 5 del examen
            
Score:      -
Versión:    0.0.1
Fixes:      -
"""

from ExamenFinal.redes_neuronales.Neurona import *
from ExamenFinal.redes_neuronales.Capa import *


if __name__ == "__main__":
    entradas = [7,21,-10]
    pesos = [-2,4.5,8.2]
    sesgo = 0.5
    
    ejercicio1 = Neurona(entradas,pesos,sesgo)
    
    print("Salida del perceptron del ejercicio1: \n"
          +str(ejercicio1.activacion()))
    
    entradas_c1 = [0.1,0.5]
    pesos_c1 = [
        [-4.8,4.6],#Pesos de la neurona 1
        [5.1,-5.2] #Pesos neurona 2
        ]
    
    sesgos_c1 = [-2.6,3.2]

    
    capa1 = Capa(entradas_c1,pesos_c1,sesgos_c1)
    #capa1.asignacion()
    
        
    entradas_c2 = capa1.salidas
    pesos_c2 = [
        [5.9,-5.2] 
    #solo un arreglo de pesos al tratarse de una neurona solamente
        ]
    sesgos_c2 = [0.5]
    
    capa2 = Capa(entradas_c2,pesos_c2,sesgos_c2)
    
    print("\nSalida del perceptron del ejecicio 2\n")
    print("Primera capa: "+str(capa1.salidas))
    print("\nResultado final tras la segunda capa de neuronas: "+str(capa2.salidas))

    
